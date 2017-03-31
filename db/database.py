from db.helpers import create_engine_uri, get_uri_params, _get_model_json

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""
Attributes
    params: A tuple with the values needed to connect to the database.
    uri (str): The uri used to connect to the database.
    engine: The object that allows for queries to be made to the database.
    db_session: 
    
Todo:
    * Complete the docstring documentation for this module.
    * Update type annotations to match PEP 484 - https://www.python.org/dev/peps/pep-0484/
    * Update instance by id
"""

params = get_uri_params()
uri = create_engine_uri(user = params[0], password = params[1], db = params[2])
engine = create_engine(uri, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=True,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()
Base._get_model_json = _get_model_json


def init_db():
    """Initializes information for the database connection.
    
    The db models are imported to register them as metadeta.
    """
    import db.models
    Base.metadata.create_all(bind=engine)


def get_all_instances(model):
    """Returns all rows for the specified model.
    
    Args:
        model: The type of model from the database that should be queried from. 
        
    Returns:
        Returns a list of items from the database of the type model is.
    """
    return db_session.query(model).all()
    
def get_instance_by_field(model, field, value):
    """Returns an instance of a model where its field matches the given value.
        
    This method expects for there only to be one query result. If
    multiple results are received from the database, an exception is
    raised.
        
    Args:
        model: The type of model from the database that should be queried from.
        field: A field that belongs to the given model. 
        value: A value that is the same type as the given field.
    
    Returns:
        Returns an instance of the model if there is a match in the 
        database, otherwise returns None.
    """
    return db_session.query(model).filter(field == value).one()
    

def get_instances_by_field(model, field, value):
    """Returns all instances of a model where its field matches the given value.
        
    Args:
        model: The type of model from the database that should be queried from.
        field: A field that belongs to the given model. 
        value: A value that is the same type as the given field.
    
    Returns:
        Returns a list of instances of type model if there is at least one
        match in the database, otherwise returns None.
    """
    return db_session.query(model).filter(field == value).all()
    

def add_instance(instance):
    """Inserts an instance of any model into the database.
    
    Args:
        instance: An instance of any of the database models.
        
    Returns: 
        Returns true if the instance is received by the database,
        otherwise returns false.
    """
    return update_model(model, instance)
    

def update_instance(instance):
    """Updates the instance of any model inside the database.
    
    Args:
        instance: An instance with info that should be updated in the database.
        
    Returns:
        Returns true if the instance is received by the database,
        otherwise returns false.
    """
    is_updated = False
    try:
        db_session.add(instance)
        is_updated = True
    except:
        # Todo: Log the error (Find specific errors that can happen)
        pass
    
    return is_updated
    

def remove_instance_by_field(model, field, value):
    """Removes an instance from the database with the given value for its field.
        
    Args:
        model: The type of model from the database that should be queried from.
        field: A field that belongs to the given model. 
        value: A value that is the same type as the given field.
    
    Returns:
        Returns true if there is an entity with that matches the value for the 
        given field in the database, otherwise returns false.
    """
    is_deleted = False
    try:
        result = db_session.query(model).filter(field == value).delete()
        
        if result == 1:
            is_deleted = True
    except:
        # Todo: Add exception cases
        pass
            
    return is_deleted