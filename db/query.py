from db.database import init_db, db_session
from db.models import User

def does_user_email_exist(email: str) -> bool:
    """Returns whether a user email exists in the database.
    
    Args:
        email: An email that may belong to a user.
    
    Returns:
        Returns true if the email exists, false otherwise.
    """
    return db_session.query(User).filter_by(email = email).first() != None