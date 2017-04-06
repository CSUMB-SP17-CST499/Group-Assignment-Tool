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
    
    employee_email = args.get('email')
    if request.method == 'GET':
        try:
            employee = query.get_employee_by_email(employee_email)
            
            if employee:
                return get_json('employee', employee)
            else:
                response = create_error('employee_not_found')
                return (response, 404)
                
        except Exception as e:
            response = create_error('unexpected_error', e)
            return (response, 500)