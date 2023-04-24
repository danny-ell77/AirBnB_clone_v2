#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""	
    return "HBNB"


@app.route("/c/<text>")
def display_c(text, strict_slashes=False):
    """Displays 'C' followed by the value of <text>
    Replaces any underscores in <text> with slashes.
    """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)

