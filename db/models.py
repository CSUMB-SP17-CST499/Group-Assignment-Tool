from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy
from db.database import Base
from db.helpers import delete_keys, get_common_pairs


class Model():

    def get_dict(self, exclude = []):
        """Returns a dictionary with the member variables of a database model.

        Only works on the first level of the model's dictionary object. If there
        is an inner dictionary, then it would not be possible to exclude single 
        keys value pairs from the inner dictionary.

        Args:
            exclude: A list containing the key value pairs to exlude. The key
                value pairs are the variable names and values of the model instance.

        Returns:
            Returns a dictionary with the instances member variables as key
            value pairs if any exist.
        """
        model_dict = {}
        d = dict(self.__dict__)
        model_dict.update(get_common_pairs(d) )
        delete_keys(model_dict, exclude)

        return model_dict

class User(Base, Model):
    """The model for the user table.

    Attributes:
        email: The user's email address. It is the primary key of the table
            and will be used for logging in to the application.
        first_name: The first name of the user.
        last_name: The last name of the user.
        username: The username the user can use to refer to themself. This can
            also be used for logging in.
        password: The password the user uses to authenticate.
        is_admin: A boolean value that used to identify whether the user is an
            admin within the app.

    """
    __tablename__ = 'user'

    email = Column(String(255), primary_key = True)
    first_name = Column(String(255) )
    last_name = Column(String(255) )
    username = Column(String(255) )
    password = Column(String(255) )
    is_admin = Column(Integer )

    def __init__(self, email: str, first_name: str, last_name: str,
            username: str , password: str, is_admin: bool = False):

        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.is_admin = is_admin


    def __repr__(self):
        str_format = '<User(email: %s, first_name: %s, last_name: %s)>'
        values = (self.email, self.first_name, self.last_name)
        return str_format % values
        
        
    def get_dict(self, exclude):
        user_dict = super(User, self).get_dict()
        


class Employee(Base, Model):
    """The model for the employee table.

    Attributes:
        email (str): The employee's email. It is used as the primary key for
            the table, and it will be used for adding employees to groups for
            the corresponding apps.
        first_name (str): The employee's first name.
        last_name (str): The employee's last name.

    """
    __tablename__ = 'employee'

    empl_id = Column(Integer)
    email = Column(String(255), primary_key = True)
    first_name = Column(String(255) )
    last_name = Column(String(255) )

    roles = association_proxy('employee_roles', 'role')


    def __init__(self, empl_id: int ,email: str, first_name: str, last_name: str):
        self.empl_id = empl_id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name


    def __repr__(self):
        str_format = '<Employee(empl_id: %d, email: %s, first_name: %s, last_name: %s)>'
        values = (self.empl_id, self.email, self.first_name, self.last_name)
        return str_format % values
    
    
    def get_dict(self, exclude = []):
        employee_dict = super(Employee, self).get_dict(exclude)
        roles = [role.get_dict() for role in self.roles]
        employee_dict.update([('roles', roles)])
        
        return employee_dict
    

class App(Base, Model):
    """The model for the app table.

    Attributes:
        app_id (int): The primary key of the app table.
        name (str): The name of the app. It is used to distinguish which
            application groups belong to, since group names may be repeated.

    """
    __tablename__ = 'app'

    app_id = Column(Integer, primary_key = True)
    name = Column(String(255) )


    def __init__(self, app_id: int, name: str, token: str = ""):
        self.app_id = app_id
        self.name = name
        self.token = token


    def __repr__(self):
        str_format = '<App(app_id: %s, name: %s)>'
        values = (self.app_id, self.name)
        return str_format % values


    def get_dict(self, exclude):
        exclude.append('token')
        return super(App, self).get_dict(exclude)


class Role(Base, Model):
    """The model for the role table.

    Attributes:
        role_id (int): The primary key of the role table.
        name (str): The name of the role. Roles must have unique names to
            make them easy to tell them apart.
        description (str): A description of the role.

    """
    __tablename__ = 'role'

    role_id = Column(Integer, primary_key = True)
    name = Column(String(255), unique = True )
    description = Column(String(1000) )
    
    groups = association_proxy('role_groups', 'group')


    def __init__(self, role_id, name, description):
        self.role_id = role_id
        self.name = name
        self.description = description


    def __repr__(self):
        str_format = '<Role(role_id: %s, name: %s, description: %s)>'
        values = (self.role_id, self.name, self.description)
        return str_format % values
    

class Group(Base, Model):
    """The model for the group table.

    Attributes:
        group_id: (int): The primary key of the group table.
        name (str): The name of a group from one of the supported applications.
            Group names may be repeated in different applications.
        app_id (int): The id of the app that this group belongs to.

    """
    __tablename__ = 'group'

    group_id = Column(Integer, primary_key = True)
    name = Column(String(255) )
    app_id = Column(Integer, ForeignKey('group.app_id'))
    app_group_id = Column(String(255) )
    

    def __init__(self, group_id, name, app_id, app_group_id):
        self.group_id = group_id
        self.name = name


    def __repr__(self):

        str_format = '<Group(group_id: %s, name: %s)>'
        values = (self.group_id, self.name)
        return str_format % values


class EmployeeToRole(Base, Model):
    """The model for the employee_role table.

    Attributes:
        email: (str): Foreign key, from the employee table.
        role_id (int): Foreign key, from the roles table.

    """
    __tablename__ = 'employee_role'

    email = Column(String(255), ForeignKey('employee.email'), primary_key = True)
    role_id = Column(Integer, ForeignKey('role.role_id'), primary_key = True)

    employee = relationship(Employee,
                backref = backref('employee_roles',
                          cascade = 'all, delete-orphan')
            )
            
    role = relationship('Role')


    def __init__(self, email, role_id):
        self.email = email
        self.role_id = role_id


    def __repr___(self):
        str_format = '<EmployeeToRole(email: %s, role_id: %d)>'
        values = (self.email, self.role_id)
        return str_format % values


class RoleToGroup(Base, Model):
    """The model for the role_group table.

    Attributes:
        group_id: (str): Foreign key, from the group_id table.
        role_id (int): Foreign key, from the roles table.
    """
    __tablename__ = 'role_group'

    group_id = Column('group_id', Integer, ForeignKey('group.group_id'), primary_key = True)
    role_id = Column('role_id', Integer, ForeignKey('role.role_id'), primary_key = True)

    role = relationship(Role,
                backref = backref('role_groups',
                          cascade = 'all, delete-orphan')
            )

    group = relationship('Group')


    def __init__(self, email, role_id):
        self.group_id = group_id
        self.role_id = role_id


    def __repr___(self):
        str_format = '<RoleToGroup(group_id: %d, role_id: %d)>'
        values = (self.group_id, self.role_id)
        return str_format % values


class AppToGroup(Base, Model):
    """The model for the app_group table.

    Attributes:
        app_id: (str): Foreign key, from the app table.
        group_id (int): Foreign key, from the group table.

    """
    __tablename__ = 'app_group'

    app_id = Column('app_id', Integer, ForeignKey('app.app_id'), primary_key = True)
    group_id = Column('group_id', Integer, ForeignKey('group.group_id'), primary_key = True)
    

    def __init__(self, app_id, role_id):
        self.app_id = app_id
        self.group_id = group_id


    def __repr___(self):
        str_format = '<AppToGroup(group_id: %d, app_id: %d)>'
        values = (self.group_id, self.app_id)
        return str_format % values
