from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    """index page"""
    return render_template('index.html')  # You can create an HTML file for the landing page

@socketio.on('message')
def handle_message(data):
    """handler for the 'message' event"""
    print('Received message:', data)
    socketio.emit('message', data)  # Echo the message back to all clients

if __name__ == '__main__':
    socketio.run(app, debug=True) # type: ignore
