from flask import Blueprint, request
from db.encode import get_json, create_error
from db import query
from db.models import Employee
from apis import slack
from synchronization import sync
import json

employees = Blueprint('employees', __name__,
                    template_folder='templates')
                    
@employees.route('/api/employee', methods = ['GET', 'PUT', 'DELETE'])
def employee_uri():
    
    args = request.get_json()
    if args is None:
        response = create_error('missing_argument')
        return (response, 404)
    
    empl_id = args.get('id')
    print(empl_id)
    excludes = args.get('excludes', [])
    if request.method == 'GET':
        try:
            employee = query.get_employee_by_id(empl_id)
            

            if employee:
                return get_json('employee', employee, excludes)

            else:
                response = create_error('employee_not_found')
                return (response, 404)
                
        except Exception as e:
            response = create_error('unexpected_error', e)
            return (response, 500)
            
    elif request.method == 'PUT':
        try:
            email = args.get('email')
            first_name = args.get('first_name')
            last_name = args.get('last_name')
            role_ids = args.get('roles')
            
            # Update the employee with the provided info
            if empl_id:
                employee = query.get_employee_by_id(empl_id)
                if employee:
                    if employee.email is None:
                        response = create_error('invalid_email')
                        return (response, 400)
                    elif employee.email != email and query.does_employee_email_exist(email):

                        response = create_error('email_taken')
                        return (response, 400)

                    if first_name:
                        employee.first_name = first_name
                    if last_name:
                        employee.last_name = last_name
                    if email:
                        employee.email = email
                    if role_ids:
                        roles = get_roles_with_ids(role_ids)
                        sync.remove_employee_from_roles(employee)
                        employee.roles = roles
                        sync.add_employee_to_roles(employee)
                    is_updated = query.update_employee(employee)
                    if is_updated:
                        return (get_json('employee', employee), 200)
                            
                    response = create_error('unexpected_error', 'Employee was not updated')
                    return (response, 500)
                else:
                    response = create_error('employee_not_found')
                    return (response, 404)

            # Insert a new employee if the right conditions are met 
            else:
                if query.does_employee_email_exist(email):
                    response = create_error('email_taken')
                    return (response, 400)
                elif email:
                    roles = get_roles_with_ids(role_ids)
                    employee = Employee(email=email,
                            first_name=first_name,
                            last_name=last_name)
                    employee.roles = roles
                    is_added = query.add_employee(employee)

                    if is_added:
                        response = get_json('employee', employee, excludes)
                        return (response, 200)
                    else:
                        raise Exception('Database operation failed: %s' % 
                                        'add into employee table')
                else:
                    response = create_error('missing_arguments')
                    return (response, 400)

        except Exception as e:
            response = create_error('unexpected_error', e)
            return (response, 500)
            
    elif request.method == 'DELETE':
        try:
            employee = query.get_employee_by_id(empl_id)
            
            if employee:
                is_deleted = query.remove_employee_by_id(empl_id)
                if is_deleted:
                    return (json.dumps({}), 200)
                
                response = create_error('unexpected_error')
                return (response, 500)
            else:
                response = create_error('unable_to_delete')
                return(response, 404)
                
        except Exception as e:
            response = create_error('unexpected_error', e)
            return (response, 500)
        

@employees.route('/api/employees', methods = ['GET', 'DELETE'])
def employees_uri():
    employee_ids = []
    
    args = request.get_json()
    if args is None and request.method == 'POST':
        response = create_error('missing_argument')
        return (response, 404)
    
    
    if request.method == 'GET':
        try:
            employees = query.get_all_employees()
            return get_json('employees', employees)
            
        except Exception as e:
            response = create_error('unexpected_error', e)
            return (response, 500)
    
    elif request.method == 'DELETE':
        try:
            employee_ids = args.get('ids', [])
            if employee_ids:
                removed_ids = remove_employees(employee_ids)
                response = json.dumps({'ids': removed_ids})
                return (response, 200)
            
        except Exception as e:
            response = create_error('unexpected_error', e)
            return (response, 500)


def get_roles_with_ids(role_ids):
    """Returns a list of Role objects with the given ids.
    
    Args:
        role_ids: A list of ids belonging to roles in the database.
        
    Returns:
        Returns a list of Role objects if a list of ids is given,
        otherwise returns an empty list.
    """ 
    if role_ids and isinstance(role_ids, list):
        return [query.get_role_by_id(role_id) \
                for role_id in role_ids]
    
    return []
    

def remove_employees(ids):
    """Removes the employees with the given employee ids.
    
    Args:
        ids: A list of employee ids belonging to employees that 
                need to be removed.
    
    Returns:
        Returns a list of employee_ids belonging to the employees that
        were removed successfully from the database.
    """
    removed = []
    for employee_id in ids:
        employee = query.get_employee_by_id(employee_id)
        
        if employee:
            is_deleted = query.remove_employee_by_id(employee.id)
        
            if is_deleted:
                removed.append(employee_id)
        
    return removed

@employees.route('/api/employee/roles', methods = ['PUT'])
def add_roles_to_employees():
    
    args = request.get_json()
    if args is None:
        response = create_error('no_args')
        return (response, 400)

    if args.get("employee_ids") is None:
        response = create_error('missing_argument', 'employee_ids argument is missing')
        return(response, 400)    
    
    if args.get("role_ids") is None:
        response = create_error('missing_argument', 'role_ids argument is missing')
        return(response, 400)

    try:
        roles = query.get_roles_with_ids(args.get("role_ids", []))
        employees = query.get_employees_with_ids(args.get("employee_ids", []))
        for role in roles:
            matching_ids = set()
            groups = query.get_role_groups(role.id)
            for group in groups:
                ids = sync.add_to_slack_group(group, employees)
                if matching_ids:
                    matching_ids.intersection(ids)
                else:
                    matching_ids = ids
            
            # Add the role to the employee when at least one of the groups was
            # added to them
            for employee in employees:
                if employee.slack_id in matching_ids:
                    employee.roles.append(role)
                    query.update_employee(employee)
            
        # TODO: Come up with the type of output we should give the client
        for matching_id in matching_ids:
            pass

        return (json.dumps({"ok": True}), 200)
    
    except Exception as e:
        response = create_error('unexpected_error', e)
        return (response, 500)

@employees.route('/api/employee/roles', methods = ['DELETE'])
def get_roles_to_delete_from_employees(): 
    
        
    args = request.get_json()
    if args is None:
        response = create_error('no_args')
        return (response, 400)

    if args.get("employee_ids") is None:
        response = create_error('missing_argument', 'employee_ids argument is missing')
        return(response, 400)    
    
    if args.get("role_ids") is None:
        response = create_error('missing_argument', 'role_ids argument is missing')
        return(response, 400)

    try:
        roles = query.get_roles_with_ids(args.get("role_ids", []))
        employees = query.get_employees_with_ids(args.get("employee_ids", []))
        for role in roles:
            groups = query.get_role_groups(role.id)
            removed_ids = set()
            for group in groups:
                ids = sync.remove_from_slack_group(group, employees)
                if ids:
                    removed_ids = removed_ids.union(ids)

            for employee in employees:
                employee.roles.remove(role)
                query.update_employee(employee)

        return (json.dumps({"ok": True}), 200)
    
    except Exception as e:
        response = create_error('unexpected_error', e)
        return (response, 500)