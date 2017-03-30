# from sqlalchemy import Column, Integer, String, Table, ForeignKey, create_engine, engine
# from db.database import Base
# from sqlalchemy.orm import sessionmaker, relationship
# from sqlalchemy.ext.declarative import declarative_base
# import models

# # Employee to role
# # app to group
# # group to role

# association_table = Table('association', Base.metadata,
#     Column('left_id', Integer, ForeignKey('left.id')),
#     Column('right_id', Integer, ForeignKey('right.id'))
# )

# class Parent(Base):
#     __tablename__ = 'left'
#     id = Column(Integer, primary_key=True)
#     children = relationship(
#         "Child",
#         secondary=association_table,
#         back_populates="parents")

# class Child(Base):
#     __tablename__ = 'right'
#     id = Column(Integer, primary_key=True)
#     parents = relationship(
#         "Parent",
#         secondary=association_table,
#         back_populates="children")

# # class Parent(Base):
# #     __tablename__ = 'left'
# #     id = Column(Integer, primary_key=True)
# #     children = relationship("Child",
# #                     secondary=association_table)

# # class Child(Base):
# #     __tablename__ = 'right'
# #     id = Column(Integer, primary_key=True)

# class employee_to_role(Base):
#     """"""
#     __tablename__ = 'employee_role'
    
#     email = Column(String(255), primary_key = True)
#     role_id = Column(Integer, primary_key = True)
 
#     #----------------------------------------------------------------------
#     def __init__(self, email, role_id):
#         """"""
#         self.email = email
#         self.role_id = role_id
 
#     #----------------------------------------------------------------------
#     def __repr__(self):
#         """"""
#         return "<'%s': '%s'>" % (self.email, self.role_id)
 
# #----------------------------------------------------------------------
# def loadSession():
#     """"""
#     metadata = Base.metadata
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     return session
 
# if __name__ == "__main__":
#     session = loadSession()
#     res = session.query(employee_to_role).all()
#     print res[0].email