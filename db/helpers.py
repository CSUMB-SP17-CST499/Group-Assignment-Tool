import os

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