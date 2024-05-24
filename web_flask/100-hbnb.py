#!/usr/bin/python3
"""
Flask Web application
"""

from flask import Flask, render_template
from models.state import State
from models.amenity import Amenity
from models import storage
app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def filters():
    """display an HTML page from static"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('100-hbnb.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)