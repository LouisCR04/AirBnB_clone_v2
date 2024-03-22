#!/usr/bin/python3
"""Displays HBNB"""

from flask import Flask

app = Flask(__name__)

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays a message"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
