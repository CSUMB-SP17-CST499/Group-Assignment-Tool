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
    if args is None:
        response = create_error('missing_argument')
        return (response, 404)
    
    email = args.get('email')
    
    if request.method == 'GET':
        try:
            employee = query.get_employee_by_email(email)
            
            if employee:
                return get_json('employee', employee)
            else:
                response = create_error('employee_not_found')
                return (response, 404)
                
        except Exception as e:
            response = create_error('unexpected_error', e)
            return (response, 500)
            
    elif request.method == 'PUT':
        try:
            first_name = args.get('first_name')
            last_name = args.get('last_name')
            
            # Update the employee with the provided info
            if email:
                employee = query.get_employee_by_email(email)
                if employee:       
                    if query.does_user_email_exist(employee):
                        response = create_error('email_taken')
                        return (response, 400)

                    if first_name:
                        employee.first_name = first_name
                    if description:
                        employee.last_name = last_name
                    
                    is_updated = query.update_employee(employee)
                    if is_updated:
                        return (get_json('employee', employee), 200)
                            
                    response = create_error('unexpected_error')
                    return (response, 500)
                else:
                    response = create_error('employee_not_found')
                    return (response, 404)
                    
            else:
                # Check for required arguments
                if first_name and last_name:
                    employee = Employee(email=email,
                        first_name=first_name, 
                        last_name=last_name )
                    query.add_employee(employee)
                    response = get_json('employee', employee)
                    return (response, 200)
                else:
                    response = create_error('missing_arguments')
                    return (response, 400)

        except Exception as e:
            print(e)
            response = create_error('unexpected_error', e)
            return (response, 500)
            
    elif request.method == 'DELETE':
        employee = query.get_employee_by_email(email)
        try:
            if employee:
                is_deleted = query.remove_role(email)
                if is_deleted:
                    return (json.dumps({}), 200)
                
                response = create_error('unexpected_error')
                return (response, 500)
            else:
                response = create_error('email_not_found')
                return (response, 404)
        except Exception as e:
            response = create_error('unexpected_error', e)
            return (response, 500)
    
    
@employees.route('/api/employees', methods = ['GET'])
def employee_uri():
    if request.method == 'GET':
        try:
            employees = query.get_all_employees()
            return get_json('employees', employees)
            
        except Exception as e:
            print(e)
            response = create_error('unexpected_error', e)
            return (response, 500)