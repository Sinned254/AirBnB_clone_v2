#!/usr/bin/python3
"""Return string when navigating to root dir"""
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


# Define the route for the cities by states page
@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    # Fetch all the State objects from the storage engine
    states = storage.all('State')
    # Sort the states by name
    states = sorted(states.values(), key=lambda state: state.name)
    # Render a HTML template with the states variable
    return render_template('8-cities_by_states.html', states=states)


# Run the app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
