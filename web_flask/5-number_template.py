#!/usr/bin/python3
"""starts a flax web application"""
# Import Flask
from flask import Flask, render_template


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


# Define the route for the number page
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    # Return a string to display on the web page
    return str(n) + ' is a number'


# Define the route for the number template page
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    # Render a HTML template with the number variable
    return render_template('5-number.html', number=n)


# Run the app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
