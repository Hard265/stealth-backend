from flask import Flask, render_template, request
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

# In-memory storage for user addresses and public keys
user_data = {}

@app.route('/')
def index():
    return render_template('index.html')  # You can create an HTML file for the landing page

@socketio.on('register')
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
