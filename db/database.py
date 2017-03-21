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
db_session = scoped_session(sessionmaker(autocommit=False,
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
