from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World form Btech CX Team!! Update Content Testing '
