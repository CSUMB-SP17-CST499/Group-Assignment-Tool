from sqlalchemy import Column, Integer, String, create_engine, engine
from db.database import Base
from sqlalchemy.orm import sessionmaker
import models

# Employee to role
# app to group
# group to role

class employee_to_role(Base):
    """"""
    __tablename__ = 'employee_role'
    
    email = Column(String(255), primary_key = True)
    role_id = Column(Integer, primary_key = True)
 
    #----------------------------------------------------------------------
    def __init__(self, email, role_id):
        """"""
        self.email = email
        self.role_id = role_id
 
    #----------------------------------------------------------------------
    def __repr__(self):
        """"""
        return "<'%s': '%s'>" % (self.email, self.role_id)
 
#----------------------------------------------------------------------
def loadSession():
    """"""
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
 
if __name__ == "__main__":
    session = loadSession()
    res = session.query(employee_to_role).all()
    print res[0].email