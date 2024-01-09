from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    address = Column(String, unique=True)
    public_key = Column(String)
  
class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True)
    sender_address = Column(String)
    receiver_address = Column(String)
    encrypted_message = Column(Text)
    delivered = Column(Integer, default=0)
