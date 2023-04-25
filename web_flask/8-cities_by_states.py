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
from models.state import State

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays 'Hello HBNB!'"""
    states = storage.all(State)
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def close_database_connection(exception):
    storage.close()


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
