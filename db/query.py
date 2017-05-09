from typing import List
from db.database import Session
from db.models import User, Employee, App, Role, Group,\
        EmployeeToRole, RoleToGroup
from db.database import get_all_instances, get_instance_by_field,\
        get_instances_by_field, add_instance, update_instance,\
        remove_instance_by_field


"""
    Todo: Verify how many entities should be queried at a time.
        This relates to how many items should be displayed at a time in the
        pages that allow users to view lists of items.
"""

def does_user_email_exist(email: str) -> bool:
    """Returns whether a user email exists in the database.
    Args:
        email: An email that may belong to a user.
    Returns:
        Returns true if the email exists, false otherwise.
    """
    return get_instance_by_field(User, User.email, email) is not None

    
def add_user(user: User) -> bool:
    """Adds a User to the user table.

    Args:
        user: An object containing an user's information.

    Returns:
        Returns true if the database transaction succeeded,
        otherwise returns false.
    """
    return add_instance(user)
    
    
def update_user(user: User) -> bool:
    """Updates an user's information in the database.

    Args:
        user: An object containing an user's information.

    Returns:
        Returns true if the database transaction succeeded,
        otherwise returns false.
    """
    return update_instance(user)    
    
def get_all_users() -> List[User]:
    """Returns a list of all users.

    Returns:
        Returns a list of User objects.
    """
    return get_all_instances(User)
    
def get_user_by_email(email: str) -> User:
    """Returns an user with the given email.

    Args:
        email: An user's email.

    Returns:
        Returns an user if an user has the email, otherwise returns None.
    """
    return get_instance_by_field(User, User.email, email) 
    
    
def get_user_by_id(id: int) -> User:
    """Returns an user with the given email.

    Args:
        email: An user's email.

    Returns:
        Returns an user if an user has the email, otherwise returns None.
    """
    return get_instance_by_field(User, User.id, id)  
    
    
def get_user_by_username(username: str) -> User:
    """Returns an user with the username email.

    Args:
        username: An user's email.

    Returns:
        Returns an user if an user has the usermail, otherwise returns None.
    """
    return get_instance_by_field(User, User.username, username) 
    
def remove_user_by_id(email: str) -> bool:
    """Removes an user from the user table.

    Args:
        email: An user's email.

    Returns:
        Returns true if an user is removed, otherwise returns false.
    """
    return remove_instance_by_field(User, User.email, email)    
    
def does_employee_email_exist(email: str) -> bool:
    """Returns whether a user email exists in the database.
    Args:
        email: An email that may belong to a user.
    Returns:
        Returns true if the email exists, false otherwise.
    """
    return get_instance_by_field(Employee, Employee.email, email) is not None

    
def is_usermane_correct(username: str) ->bool:
    """Returns whether a user email exists in the database.

    Args:
        email: An email that may belong to a user.

    Returns:
        Returns true if the email exists, false otherwise.
    """
    session = Session()
    return session.query(User).filter_by(username = username).first() != None

def is_password_correct(password: str) ->bool:
    """Returns whether a user email exists in the database.

    Args:
        email: An email that may belong to a user.

    Returns:
        Returns true if the email exists, false otherwise.
    """
    session = Session()
    return session.query(User).filter_by(password = password).first() != None

def does_role_name_exist(name: str) -> bool:

    """Returns whether a rolel exists in the database.

    Args:
        name: A name that may belong to a role.

    Returns:
        Returns true if the name exists, false otherwise.
    """
    return get_instance_by_field(Role, Role.name, name) is not None



def get_all_apps() -> List[App]:
    """Returns a list of all apps"""
    return get_all_instances(App)


def get_app_by_id(app_id: int):
    """Returns an app with the matching id.

    Args:
        app_id: The id to search an app by.

    Returns:
        Returns an App object with the given id if it exists, otherwise
        returns None.
    """
    return get_instance_by_field(App, App.id, app_id)


def add_app(app: App) -> bool:
    """Adds an app to the app table.

    Args:
        app: An object used to store information on external applications.

    Returns:
        Returns true if the database transaction succeeded,
        otherwise returns false.
    """
    return add_instance(app)


def update_app(app: App) -> bool:
    """Updates the values of an app in the database.

    Args:
        app: An object used to store information on external applications.

    Returns:
        Returns true if the database transaction succeeded,
        otherwise returns false.
    """
    return update_instance(app)


def remove_app(app_id: int) -> bool:
    """Removes the app with the specified id from the database.

    Args:
        app_id: The id of the app to be removed.

    Returns:
        Returns true if an app is removed, false otherwise.
    """
    return remove_instance_by_field(App, App.id, app_id)


def get_all_employees() -> List[Employee]:
    """Returns a list of all employees.

    Returns:
        Returns a list of Employee objects.
    """
    return get_all_instances(Employee)


def get_employee_by_email(email: str) -> Employee:
    """Returns an employee with the given email.

    Args:
        email: An employee's email.

    Returns:
        Returns an employee if an employee has the email, otherwise returns None.
    """
    return get_instance_by_field(Employee, Employee.email, email)
    
    
def get_employee_by_id(employee_id: int) -> Employee:
    """Returns an employee with the given email.

    Args:
        employee_id: An employee's id.

    Returns:
        Returns an employee if an employee has the email, otherwise returns None.
    """
    return get_instance_by_field(Employee, Employee.id, employee_id)


def add_employee(employee: Employee) -> bool:
    """Adds an employee to the employee table.

    Args:
        employee: An object containing an employee's information.

    Returns:
        Returns true if the database transaction succeeded,
        otherwise returns false.
    """
    return add_instance(employee)


def update_employee(employee: Employee) -> bool:
    """Updates an employee's information in the database.

    Args:
        employee: An object containing an employee's information.

    Returns:
        Returns true if the database transaction succeeded,
        otherwise returns false.
    """
    return update_instance(employee)


def remove_employee_by_id(employee_id: int) -> bool:
    """Removes an employee from the employee table.

    Args:
        email: An employee's email.

    Returns:
        Returns true if an employee is removed, otherwise returns false.
    """
    return remove_instance_by_field(Employee, Employee.id, employee_id)

def remove_role_by_id(role_id: str) -> bool:
    """Removes an employee from the employee table.

    Args:
        email: An employee's email.

    Returns:
        Returns true if an employee is removed, otherwise returns false.
    """
    return remove_instance_by_field(Role, Role.id, role_id)
    
def get_all_roles() -> List[Role]:
    """Returns a list of all roles.

    Returns:
        Returns a list of Role objects.
    """
    return get_all_instances(Role)


def get_role_by_id(role_id: int) -> Role:
    """Returns a role with the given id.

    Args:
        role_id: The id of a role.

    Returns:
        Returns a role with the given role_id,
        otherwise returns None.
    """
    return get_instance_by_field(Role, Role.id, role_id)


def add_role(role: Role) -> bool:
    """Add a role to the role table.

    Args:
        role: An object with the information for a role.

    Returns:
        Returns true if the database transaction succeeded,
        otherwise returns false.
    """
    return add_instance(role)


def update_role(role: Role) -> bool:
    """Updates the information for a role.

    Args:
        role: An object with the information for a role.

    Returns:
        Returns true if the database transaction succeeded,
        otherwise returns false.
    """
    return update_instance(role)


def remove_role(role_id: int) -> bool:
    """Removes a role from the role table.

    Args:
        role_id: The id of a role.

    Returns:
        Returns true if a role is removed, otherwise returns false.
    """
    return remove_instance_by_field(Role, Role.id, role_id)


def get_all_groups() -> List[Group]:
    """Returns a list of all groups.

    Returns:
        Returns a list of Group objects.
    """
    return get_all_instances(Group)


def get_group_by_id(group_id: int) -> Group:
    """Returns a group with the given id.

    Args:
        group_id: The id of a group.

    Returns:
        Returns a group with the given role_id,
        otherwise returns None.
    """
    return get_instance_by_field(Group, Group.id, group_id)


def add_group(group: Group) -> bool:
    """Adds a group to the group table.

    Args:
        group: An object with the information for a group.

    Returns:
        Returns true if the database transaction succeeded,
        otherwise returns false.
    """
    return add_instance(group)


def update_group(group: Group) -> bool:
    """Updates the information for a group.

    Args:
        group: An object with the information for a group.

    Returns:
        Returns true if the database transaction succeeded,
        otherwise returns false.
    """
    return update_instance(group)


def remove_group(group_id: int) -> bool:
    """Removes a group from the role table.

    Args:
        role_id: The id of a group.

    Returns:
        Returns true if a group is removed, otherwise returns false.
    """
    return remove_instance_by_field(Group, Group.id, group_id)


def get_employee_roles(email: str) -> List[EmployeeToRole]:
    """Returns a list of roles with the given email.

    Args:
        email: An employee's email.

    Returns:
        Returns a list of roles if an employee has the email, otherwise returns None.
    """
    session = Session()
    return session.query(EmployeeToRole).filter(EmployeeToRole.email == email).all()


def delete_multiple_employees(ids: List[int]) -> bool:
    """Removes all employees with a matching id.
    
    Args:
        ids: A list of ids belonging to employees.
    """
    pass
    

def get_slack_groups() -> List[Group]:
    """Returns a list of groups that belong to Slack.
    
    Returns:
        Returns a list containing all the groups from Slack.
    """
    groups = None
    session = Session()
    try:
        groups = session.query(Group).filter(Group.app_id == 1).all()
    except Exception as e:
        print(e)
        
    return groups