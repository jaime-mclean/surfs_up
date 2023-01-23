# Import dependencies

from flask import Flask

# Create New Flask app instance

app = Flask(__name__)

@app.route('/')

def hello_world():
    
    return 'Hello world'