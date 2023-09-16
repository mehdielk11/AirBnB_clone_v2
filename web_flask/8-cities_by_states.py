#!/usr/bin/python3
"""
    Start Flask web application with HBNB data
    Route /states_list displays HTML page with States listed alphabetically
    Route /cities_by_states to display webpage listing each city in each state
"""
from flask import Flask, render_template
from models import storage, classes
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """
        Route /states_list displays HTML page with States listed alphabetically
    """
    states = storage.all(classes["State"]).values()
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """
        Route /cities_by_states displays HTML listing each city in each state
    """
    states = storage.all(classes["State"]).values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """
        Function to remove SQLAlchemy Session
    """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
