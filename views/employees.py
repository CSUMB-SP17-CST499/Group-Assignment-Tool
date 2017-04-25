from flask import Blueprint, request
from db.encode import get_json, create_error
from db import query
from db.models import Employee
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
                        employee.roles = roles                    
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
            if empl_id:
                for x in empl_id:
                    employee = query.remove_employee_by_id(x)
                return ("Success", 200)
            if employee:
                is_deleted = query.remove_employee_by_id(empl_id)
                role_deleted = query.remove_employee_role_by_id(empl_id)
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
        

@employees.route('/api/employees', methods = ['GET'])
def employees_uri():
    if request.method == 'GET':
        try:
            employees = query.get_all_employees()
            return get_json('employees', employees)
            
        except Exception as e:
            print(e)
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