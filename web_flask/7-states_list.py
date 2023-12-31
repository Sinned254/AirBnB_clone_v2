#!/usr/bin/python3
"""return String when navigating to root dir"""
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


# Define the route for the states list page
@app.route('/states_list', strict_slashes=False)
def states_list():
    # Fetch all the State objects from the storage engine
    states = storage.all('State')
    # Sort the states by name
    states = sorted(states.values(), key=lambda state: state.name)
    # Render a HTML template with the states variable
    return render_template('7-7-7-7-7-7-7-states_list.html', states=states)


# Run the app on 0.0.0.0, port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
