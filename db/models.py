from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.associationproxy import association_proxy
from db.database import Base
from db.helpers import filter_dictionary


class Model():

    def get_dict(self, excludes = []):
        """Returns a dictionary with the member variables of a database model.

        Exluding only works on the first level of the model's dictionary object. 
        If there is an inner dictionary, it is not currently be possible to 
        excludes single keys value pairs from the inner dictionary.

        Args:
            excludes: A list containing the key value pairs to exlude. The key
                value pairs are the variable names and values of the model instance.

        Returns:
            Returns a dictionary with the instances member variables as key
            value pairs if any exist.
        """
        return filter_dictionary(dict(self.__dict__), excludes )

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

    email = Column('email', String(255), primary_key = True)
    first_name = Column('first_name', String(255) )
    last_name = Column('last_name', String(255) )
    username = Column('username', String(255) )
    password = Column('password', String(255) )
  #  is_admin = Column('is_admin', Integer)

    def __init__(self, email: str, first_name: str, last_name: str,
            username: str , password: str):

        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
       # self.is_admin = is_admin, , is_admin: int


    def __repr__(self):
        str_format = '<User(email: %s, first_name: %s, last_name: %s)>'
        values = (self.email, self.first_name, self.last_name)
        return str_format % values
        
        
    def get_dict(self, excludes = []):
        user_dict = super().get_dict(excludes)
        return user_dict


class Employee(Base, Model):
    """The model for the employee table.

    Attributes:
        id: The employee's id. It serves as a primary key.
        email: The employee's email.
        first_name: The employee's first name.
        last_name: The employee's last name.

    """
    __tablename__ = 'employee'

    id = Column('empl_id', Integer)
    email = Column('email', String(255), primary_key = True)
    first_name = Column('first_name', String(255) )
    last_name = Column('last_name', String(255) )
    roles = association_proxy('employee_roles', 'role')


    def __init__(self, id: int ,email: str, first_name: str, last_name: str):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name


    def __repr__(self):
        str_format = '<Employee(id: %d, email: %s, first_name: %s, last_name: %s)>'
        values = (self.id, self.email, self.first_name, self.last_name)
        return str_format % values
    
    
    def get_dict(self, excludes = []):
        employee_dict = super().get_dict(excludes)
        
        if 'roles' not in excludes:
            roles = [role.get_dict() for role in self.roles]
            employee_dict.update([('roles', roles)])
        
        return employee_dict
    

class App(Base, Model):
    """The model for the app table.

    Attributes:
        id (int): The primary key of the app table.
        name (str): The name of the app. It is used to distinguish which
            application groups belong to, since group names may be repeated.

    """
    __tablename__ = 'app'

    id = Column('app_id', Integer, primary_key = True)
    name = Column('name', String(255) )


    def __init__(self, id: int, name: str, token: str = ""):
        self.id = id
        self.name = name
        self.token = token


    def __repr__(self):
        str_format = '<App(id: %s, name: %s)>'
        values = (self.id, self.name)
        return str_format % values


    def get_dict(self, excludes):
        excludes.append('token')
        return super().get_dict(excludes)


class Role(Base, Model):
    """The model for the role table.

    Attributes:
        id (int): The primary key of the role table.
        name (str): The name of the role. Roles must have unique names to
            make them easy to tell them apart.
        description (str): A description of the role.

    """
    __tablename__ = 'role'

    id = Column('role_id', Integer, primary_key = True)
    name = Column('name', String(255), unique = True )
    description = Column('description', String(1000) )
    
    groups = association_proxy('role_groups', 'group')


    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description


    def __repr__(self):
        str_format = '<Role(id: %s, name: %s, description: %s)>'
        values = (self.id, self.name, self.description)
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

    id = Column('group_id', Integer, primary_key = True)
    name = Column('name', String(255) )
    app_group_id = Column('app_group_id', String(255) )
    

    def __init__(self, group_id, name, app_group_id):
        self.id = id
        self.name = name

        self.app_group_id = app_group_id
    
    def __repr__(self):
        str_format = '<Group(id: %s, name: %s)>'
        values = (self.id, self.name)
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
            
    role = relationship('Role', lazy='subquery')


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


    def __init__(self, group_id, role_id):
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
    

    def __init__(self, app_id, group_id):
        self.app_id = app_id
        self.group_id = group_id


    def __repr___(self):
        str_format = '<AppToGroup(group_id: %d, app_id: %d)>'
        values = (self.group_id, self.app_id)
        return str_format % values
