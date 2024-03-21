#!/usr/bin/python3
"""Starts a Flask Web App"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hbnb():
    """Displays a message"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0:5000")
