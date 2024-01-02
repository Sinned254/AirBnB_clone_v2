#!/usr/bin/python3
"""  script that starts a Flask web application:"""
# Import Flask, render_template, and storage
from flask import Flask, render_template
from models import storage

# Create an instance of Flask
app = Flask(__name__)


# Define a method to handle app teardown
@app.teardown_appcontext
def teardown_db(exception):
    # Close the current SQLAlchemy Session
    storage.close()


# Define the route for the hbnb filters page
@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    # Fetch all the State and Amenity objects from the storage engine
    states = storage.all('State')
    amenities = storage.all('Amenity')
    # Sort the states and amenities by name
    states = sorted(states.values(), key=lambda state: state.name)
    amenities = sorted(amenities.values(), key=lambda amenity: amenity.name)
    # Render a HTML template with the states and amenities variables
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


# Run the app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)