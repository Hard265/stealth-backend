# registration_handler.py

user_data = {}  # Assuming user_data is a global dictionary

def handle_registration(data):
    """
    Event handler for user registration.
    Expects data to contain 'address' and 'public_key'.
    """
    address = data.get('address')
    public_key = data.get('public_key')

    if address and public_key:
        user_data[address] = public_key
        print(f"User registered: {address}")
