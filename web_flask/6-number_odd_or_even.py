from flask import Flask, render_template

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


@app.route("/number/<int:n>")
def number_n(n):
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def html_route(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def number_odd_or_even(n):
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
