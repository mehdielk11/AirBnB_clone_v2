#!/usr/bin/python3
"""
    Start Flask web application that listens on 0.0.0.0:5000
    Has route / that displays "Hello HBNB!"
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """
        Route / displays "Hello HBNB!"
    """
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run()
