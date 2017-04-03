from typing import List
from db.database import Session
from db.models import User, Employee, App, Role, Group,\
        EmployeeToRole, RoleToGroup, AppToGroup
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
    session = Session()
    return session.query(User).filter_by(email = email).first() != None


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
    return get_instance_by_field(App, App.app_id, app_id)


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
    return remove_instance_by_field(App, App.app_id, app_id)


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


def remove_employee(email: str) -> bool:
    """Removes an employee from the employee table.

    Args:
        email: An employee's email.

    Returns:
        Returns true if an employee is removed, otherwise returns false.
    """
    return remove_instance_by_field(Employee, Employee.email, email)


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
    return get_instance_by_field(Role, Role.role_id, role_id)


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
    return remove_instance_by_field(Role, Role.role_id, role_id)


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
    return get_instance_by_field(Group, Group.group_id, group_id)


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
    return remove_instance_by_field(Group, Group.group_id, group_id)


def get_employee_roles(email: str) -> List[EmployeeToRole]:
    """Returns a list of roles with the given email.

    Args:
        email: An employee's email.

    Returns:
        Returns a list of roles if an employee has the email, otherwise returns None.
    """
    session = Session()
    return session.query(EmployeeToRole).filter(EmployeeToRole.email == email).all()


def get_all_employees_with_roles() -> List[EmployeeToRole]:
    session = Session()
    return session.query(Employee, Role).filter(Employee.email == EmployeeToRole.email).filter(Role.role_id == EmployeeToRole.role_id).all()


def get_all_groups_with_roles() -> List[RoleToGroup]:
    session = Session()
    return session.query(Group, Role).filter(Group.group_id == RoleToGroup.group_id).filter(Role.role_id == RoleToGroup.role_id).all()


def get_all_apps_with_groups() -> List[AppToGroup]:
    session = Session()
    return session.query(App, Group).filter(Group.group_id == AppToGroup.group_id).filter(App.app_id == AppToGroup.app_id).all()
