#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
app = Flask(__name__)


@app.template_filter('odd_or_even')
def oddeven(n):
    """check if number is odd or even"""
    if n % 2 == 0:
        return f"{n} is even"
    else:
        return f"{n} is odd"


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """display a HTML page only if n is an integer"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
