from flask import Blueprint, request, g
from db.encode import get_json, create_error
from db import query
from werkzeug.security import generate_password_hash, \
     check_password_hash
from db.models import User
from flask_login import login_user , logout_user , current_user , login_required
import json

users = Blueprint('user', __name__,
                    template_folder='templates')
                    
@users.route('/api/user', methods = ['POST', 'PUT', 'DELETE'])
def user_uri():
    #args = request.args
    # print(request.args)
    print(request.get_json())
    # print(request.data)
    args = request.get_json()
    if args is None:
        response = create_error('missing_argument')
        return (response, 404)
    
    user_email = args.get('email')
    # password = args.get('password')
    # if password:
    #     hashedpw = generate_password_hash(password)

    #Get the post call from login.js and verify that it is correct, does not left user 
    # login if they entered the wrong things
    excludes = args.get('excludes', [])
    if request.method == 'POST':
        username = args.get('username')
        password = args.get('password')
        print(username)
        try:
            user = query.get_user_by_username(username)
            print(user)
            if user:
                if (query.is_usermane_correct(user.username)):
                    print(user.username)
                    if (check_password_hash(user.password, password)):
                        print(login_user(user))
                        print(current_user)
                        #TODO create a session varaible that makes it so the user can acess pages that
                        #normally would not be allowed to acess such as add, edit or delete any users
                        return get_json('user', user, excludes)
                    else:
                        response = create_error('password is incorrect')
                        return (response, 404)
                else:
                    response = create_error('username is incorrect')
                    return (response, 404)        

            else:
                response = create_error('user_not_found')
                return (response, 403)
                
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
            if password:
                hashedpw = generate_password_hash(password)
            isadmin_checkbox = args.get('is_admin')
            if isadmin_checkbox in 'on':
                isadmin = 1
            else:
                isadmin = 0
            
            #Update the user with the provided info
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
                     password = password
                if isadmin:
                    user.isadmin = isadmin    

                    
                    is_updated = query.update_user(user)
                    if is_updated:
                        return (get_json('user', user), 200)
                            
                    response = create_error('unexpected_error', 'Employee was not updated')
                    return (response, 500)
                else:
                    response = create_error('employee_not_found')
                    return (response, 404)

            # Insert a new user if the right conditions are met 
            if user_email:
                if query.does_user_email_exist(user_email):
                    response = create_error('email_taken')
                    return (response, 400)         
                elif email:
                    #hashpassword = hashPassword(password)
                    user = User( 
                        email=email,
                        first_name=first_name,
                        last_name=last_name, 
                        username = username,
                        password = hashedpw,
                        is_admin = isadmin)
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
            