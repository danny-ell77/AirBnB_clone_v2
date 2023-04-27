#!/usr/bin/python3
"""Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
"""
from flask import Flask
from flask import render_template

from models import storage
from models import State, Amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Displays 'Hello HBNB!'"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


@app.teardown_appcontext
def close_database_connection(exception):
    """This function closes the db session when the application context ends"""
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
