from sqlalchemy import Column, Integer, String, create_engine
from db.database import Base
from sqlalchemy.orm import sessionmaker
import models

# Employee to role
# app to group
# group to role

class employee_to_role(Base):
    """"""
    __tablename__ = 'employee'
    
    email = Column(String(255), primary_key = True)
    first_name = Column(String(255) )
    last_name = Column(String(255) )
 
    #----------------------------------------------------------------------
    def __init__(self, id, url, title, rev_host, visit_count,
                 hidden, typed, favicon_id, frecency, last_visit_date):
        """"""
        self.id = id
        self.url = url
        self.title = title
        self.rev_host = rev_host
        self.visit_count = visit_count
        self.hidden = hidden
        self.typed = typed
        self.favicon_id = favicon_id
        self.frecency = frecency
        self.last_visit_date = last_visit_date
 
    #----------------------------------------------------------------------
    def __repr__(self):
        """"""
        return "<Places - '%s': '%s' - '%s'>" % (self.id, self.title,
                                                 self.url)
 
#----------------------------------------------------------------------
def loadSession():
    """"""
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
 
if __name__ == "__main__":
    session = loadSession()
    res = session.query(Places).all()
    print res[1].title