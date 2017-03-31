from db.helpers import create_engine_uri, get_uri_params

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
"""

params = get_uri_params()
uri = create_engine_uri(user = params[0], password = params[1], db = params[2])
engine = create_engine(uri, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=True,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    """Initializes information for the database connection.
    
    The db models are imported to register them as metadeta.
    """
    import db.models
    Base.metadata.create_all(bind=engine)


def get_all_models(model):
    """Returns all rows for the specified model.
    
    Args:
        model: The type of model from the database that should be queried from. 
        
    Returns:
        Returns a list of items from the database of the type model is.
    """
    return db_session.query(model).all()
    
def get_model_by_field(model, field, value):
    """Returns an instance of a model where its field matches the given value.
        
    This method expects for there only to be one query result. If
    multiple results are received from the database, an exception is
    raised.
        
    Args:
        model: The type of model from the database that should be queried from.
        field: A field that belongs to the given model. 
        value: A value that is a type of the given field.
    
    Returns:
        Returns an instance of the model if there is a match in the 
        database, otherwise returns None.
    """
    return db_session.query(model).filter(field == value).one()
    

def get_models_by_field(model, field, value):
    """Returns all instances of a model where its field matches the given value.
        
    Args:
        model: The type of model from the database that should be queried from.
        field: A field that belongs to the given model. 
        value: A value that is a type of the given field.
    
    Returns:
        Returns a list of instances of type model if there is at least one
        match in the database, otherwise returns None.
    """
    return db_session.query(model).filter(field == value).all()