from flask import request
from app import app
from database import create_engine_and_session, add_user_to_database

db_url = "postgresql://username:password@localhost:5432/database_name"
session = create_engine_and_session(db_url)

@app.route('/register', methods=['POST'])
def register_user(data):
  address = data.get('address')
  public_key = data.get('public_key')

  if not address or not public_key:
    return "Missing address or public_key in the data", 400

    # Check if the user is already registered
  if session.query(User).filter_by(address=address).first():
    return "User already registered with this address", 409

    # Save user to the database
  add_user_to_database(session, address, public_key)
  return "Registration successful", 200 
