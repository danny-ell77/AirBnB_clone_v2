from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def display_c(text, strict_slashes=False):
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", defaults={"text": "is_cool"})
@app.route("/python/<text>")
def display_python(text="is_cool", strict_slashes=False):
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
