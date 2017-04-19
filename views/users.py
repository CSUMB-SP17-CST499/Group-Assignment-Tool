from flask import Blueprint, request
from db.encode import get_json, create_error
from db import query, hashPassword
from db.models import User
import json

users = Blueprint('user', __name__,
                    template_folder='templates')
                    
@users.route('/api/user', methods = ['GET', 'PUT', 'DELETE'])
def user_uri():
    args = request.args
    # print(request.args)
    print(request.get_json())
    # print(request.data)
    args = request.get_json()
    if args is None:
        response = create_error('missing_argument')
        return (response, 404)
    
    user_email = args.get('email')
    excludes = args.get('excludes', [])
    if request.method == 'GET':
        try:
            user = query.get_user_by_email(user_email)

            if user:
                return get_json('user', user, excludes)

            else:
                response = create_error('user_not_found')
                return (response, 404)
                
        except Exception as e:
            response = create_error('unexpected_error', e)
            return (response, 500)
            
    elif request.method == 'PUT':
        try:
            email = args.get('email')
            first_name = args.get('first_name')
            last_name = args.get('last_name')
            username = args.get('username')
            password = args.get('password')
            isadmin = args.get('is_admin')
            
            # Update the user with the provided info
            if user_email:
                user = query.get_user_by_email(user_email)
                if user:
                    if user.email is None:
                        response = create_error('invalid_email')
                        return (response, 400)
                    elif user.email != email and query.does_user_email_exist(email):

                        response = create_error('email_taken')
                        return (response, 400)

                    if first_name:
                        user.first_name = first_name
                    if last_name:
                        user.last_name = last_name
                    if email:
                        user.email = email
                    if username:
                        user.username = username
                    if password:
                         hashpassword = hashPassword(password)
                    if isadmin:
                        user.isadmin = isadmin    
                    # if roles:
                    #     pass # Todo: Handle updated roles

                    
                    is_updated = query.update_user(user)
                    if is_updated:
                        return (get_json('user', user), 200)
                            
                    response = create_error('unexpected_error', 'Employee was not updated')
                    return (response, 500)
                else:
                    response = create_error('employee_not_found')
                    return (response, 404)

            # Insert a new user if the right conditions are met 
            else:
                if query.does_employee_email_exist(email):
                    response = create_error('email_taken')
                    return (response, 400)         
                elif email:
                    user = User( 
                        email=email,
                        first_name=first_name,
                        last_name=last_name, 
                        username = username,
                        password = hashpassword,
                        isadmin = isadmin)
                    query.add_user(user)

                    response = get_json('user', user, excludes)
                    return (response, 200)
                else:
                    response = create_error('missing_arguments')
                    return (response, 400)

        except Exception as e:
            response = create_error('unexpected_error', e)
            return (response, 500)
            
    elif request.method == 'DELETE':
        user = query.get_user_by_email(email)
        try:
            if user:
                is_deleted = query.remove_user_by_id(email)
                if is_deleted:
                    return (json.dumps({}), 200)
                
                response = create_error('unexpected_error')
                return (response, 500)
            else:
                response = create_error('employee_not_found')
                return (response, 404)
        except Exception as e:
            response = create_error('unexpected_error', e)
            return (response, 500)
    
    
@users.route('/api/users', methods = ['GET'])
def users_uri():
    if request.method == 'GET':
        try:
            users = query.get_all_users()
            return get_json('users', users)
            
        except Exception as e:
            print(e)
            response = create_error('unexpected_error', e)
            return (response, 500)
            