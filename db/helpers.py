import os
from typing import List

"""
Todo:
    * Create input validation for the create_engine_uri function
    * Update type annotations to match PEP 484 - https://www.python.org/dev/peps/pep-0484/
"""

def get_uri_params():
    """Returns the values neeeded to connect to a MySQL database."""
    username = os.getenv('DB_USER')
    password = os.getenv('DB_USER_PASSWORD')
    database = os.getenv('DB_NAME')

    return (username, password, database)


def create_engine_uri(user, password, db, host = 'localhost'):
    """Creates the uri for accessing a MySQL database.

    Args:
        user (str): The username of the application user.
        password (str): The password belonging to the user.
        database (str): The name of the database to connect to.
        host (str): The ip address the database is hosted on.
            Defaults to localhost.
    """
    return 'mysql+pymysql://%s:%s@%s/%s' % (user, password, host, db)




def delete_keys(d: dict, keys: List[str]):
    """Removes the given keys from the dictionary.
    
    Args:
        dictionary: A builtin python dictionary.
        keys: A list of possible dictionary key names to
            be removed from the dictionary.
    """
    for key in keys:
        if key in d:
            del d[key]
            
            
def filter_dictionary(d: dict, excludes = []) -> dict:
    """Returns a list of key value pairs from common value types.
    
    Args:
        d: A python dictionary.
        
    Returns: 
        Returns a list of tuples if there are values of the
        common data types.
    """
    new_dict = {}
    for key in d.keys():
        val = d[key]
        if is_common_type(val) and val not in excludes:
            new_dict.update([(key, val)])

    return new_dict
    
    
def is_common_type(value) -> bool:
    """Returns whether a value is a common python object type 
    
    Args:
        value: A python object.
        
    Returns: 
        Returns true if the value is a common python data type. 
        e.g. int, bool, str
    """
    return isinstance(value, (int, bool, str) )