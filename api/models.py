from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    address = Column(String, unique=True)
    public_key = Column(String)