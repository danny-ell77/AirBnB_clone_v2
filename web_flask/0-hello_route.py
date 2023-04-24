#!/usr/bin/python3
"""This script runs a simple flask application server
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
"""Displays 'Hello HBNB!'"""


def hello():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
