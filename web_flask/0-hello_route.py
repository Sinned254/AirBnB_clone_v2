#!/usr/bin/python3
"""Return string wnen navigatiind root dir"""
from flask import Flask

# Create an instance of Flask
app = Flask(__name__)


# Define the route for the index page
@app.route('/', strict_slashes=False)
def hello_index():
    # Return a string to display on the web page
    return 'Hello HBNB!'


# Run the app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
