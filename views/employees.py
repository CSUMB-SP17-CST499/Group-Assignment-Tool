from flask import Blueprint, request
from db.encode import get_json, create_error
from db import query
from db.models import Employee
import json

employees = Blueprint('employees', __name__,
                    template_folder='templates')
                    
@employees.route('/api/employee', methods = ['GET', 'PUT', 'DELETE'])
def employee_uri():
    args = request.args
    # print(request.args)
    print(request.get_json())
    # print(request.data)
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
            roles = args.get('roles')
            
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
                    employee = Employee(None, 
                        email=email,
                        first_name=first_name,
                        last_name=last_name)
                    query.add_employee(employee)

                    response = get_json('employee', employee, excludes)
                    return (response, 200)
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
            