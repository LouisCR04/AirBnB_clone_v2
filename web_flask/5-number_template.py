#!/usr/bin/python3
"""
Displays a HTML page only if n is an integer:
H1 tag: “Number: n” inside the tag BODY
"""

from flask import Flask

app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays a message"""
    return "Hello HBNB!"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    return f"C {text.replace('_',' ')}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    return f"Python {text.replace('_', ' ')}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>:", strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
