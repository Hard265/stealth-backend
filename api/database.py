# database.py
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .models import Base

def create_engine_and_session(db_url):
    engine = create_engine(db_url)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    return Session()

def add_user_to_database(session, address, public_key):
    new_user = User(address=address, public_key=public_key)
    session.add(new_user)
    session.commit()
