#!/usr/bin/python3
"starts flask web appliucation"""
from flask import Flask


# Create an instance of Flask
app = Flask(__name__)


# Define the route for the index page
@app.route('/', strict_slashes=False)
def index():
    # Return a string to display on the web page
    return 'Hello HBNB!'


# Define the route for the hbnb page
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    # Return a string to display on the web page
    return 'HBNB'


# Define the route for the c page
@app.route('/c/<text>', strict_slashes=False)
def c(text):
    # Replace underscore with space in the text variable
    text = text.replace('_', ' ')
    # Return a string to display on the web page
    return 'C ' + text


# Define the route for the python page
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    # Replace underscore with space in the text variable
    text = text.replace('_', ' ')
    # Return a string to display on the web page
    return 'Python ' + text


# Run the app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
