#!/usr/bin/python3
"""
    Start Flask web application that listens on 0.0.0.0:5000
    Has route / that displays "Hello HBNB!"
    Has route /hbnb that displays "HBNB"
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
        Route / displays "Hello HBNB!"
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
        Route /hbnb displays "HBNB!"
    """
    return 'HBNB'


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
