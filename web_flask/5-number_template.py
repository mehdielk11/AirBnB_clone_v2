#!/usr/bin/python3
"""
    Start Flask web application that listens on 0.0.0.0:5000
    Has route / that displays "Hello HBNB!"
    Has route /hbnb that displays "HBNB"
    Has route /c/<text> displays C followed by text
    Has route /python/<text> that displays Python + text
        Default value of text = "is cool"
    Has route /number/<n> that displays 'n is a number' if n is an integer
    Add route /number_template/<n> to display HTML only if n is an integer
"""
from flask import Flask, render_template
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


@app.route('/c/<text>', strict_slashes=False)
def cprint(text):
    """
        Route /c/<text> displays C followed by text
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def pyprint(text="is cool"):
    """
        Route /python/<text> displays Python followed by text
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def nprint(n):
    """
        Route /number/<n> that displays 'n is a number' if n is an integer
    """
    return "{:d} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def ntemplate(n):
    """
        Route /number_template/<n> that displays webpage if n is an integer
    """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
