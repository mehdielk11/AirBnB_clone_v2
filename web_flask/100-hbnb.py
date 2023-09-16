#!/usr/bin/python3
"""
    Route /hbnb to display HBNB HTML page
"""
from flask import Flask, render_template
from models import storage, classes
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb_filters():
    """
        Route /hbnb to display HBNB HTML page
    """
    states = storage.all(classes["State"]).values()
    amenities = storage.all(classes["Amenity"]).values()
    places = storage.all(classes["Place"]).values()
    for place in places:
        print(place.name)
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities, place=places)


@app.teardown_appcontext
def teardown_db(exception):
    """
        Function to remove SQLAlchemy Session
    """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
