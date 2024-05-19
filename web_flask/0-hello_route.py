#!/usr/bin/python3
"""Create instanc of WSGI app from flask class"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """flask mini app"""
    return f"Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
