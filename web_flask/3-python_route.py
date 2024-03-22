#!/usr/bin/python3
"""
Displays “Python ”, followed by
the value of the text variable
(replace underscore _ symbols with a space )
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
def python(text="cool"):
    return f"Python {text.replace('_', ' ')}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
