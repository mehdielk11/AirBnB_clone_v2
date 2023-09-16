#!/usr/bin/python3
"""
    Start Flask web application with HBNB data
    Route /hbnb_filters to display HBNB HTML page
"""
from flask import Flask, render_template
from models import storage, classes
app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
        Route /hbnb_filters to display HBNB HTML page
    """
    states = storage.all(classes["State"]).values()
    amenities = storage.all(classes["Amenity"]).values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """
        Function to remove SQLAlchemy Session
    """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
