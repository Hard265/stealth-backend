from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# In-memory storage for user addresses and public keys
user_data = {}

@app.route('/')
def index():
    return render_template('index.html')  # You can create an HTML file for the landing page

@app.router('/register')
def registration(data):
    """
    Event handler for user registration.
    Expects data to contain 'address' and 'public_key'.
    Returns a tuple with a response message and status code.
    """
    address = data.get('address')
    public_key = data.get('public_key')

    if not address or not public_key:
        return "Missing address or public_key in the data", 400

    # Check if the user is already registered
    if session.query(User).filter_by(address=address).first():
        return "User already registered with this address", 409

    # Save user to the database
    add_user_to_database(session, address, public_key)

    print(f"User registered: {address}")

    return "Registration successful", 200


@socketio.on('login')
def handle_login(data):
    """
    Event handler for user login.
    Expects data to contain 'address' and 'challenge_signature'.
    """
    address = data.get('address')
    challenge_signature = data.get('challenge_signature')

    if address and challenge_signature:
        # Verify the challenge signature using the stored public key
        public_key = user_data.get(address)
        if public_key:
            # Implement signature verification logic here (depends on your crypto library)
            # If verification is successful, the user is authenticated
            print(f"User {address} logged in")
        else:
            print(f"User {address} not found")

if __name__ == '__main__':
    socketio.run(app, debug=True)
