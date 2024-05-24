#!/usr/bin/python3
"""Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """display states and cities"""
    states = storage.all(State)
    state_id = ""
    if id is not None:
        state_id = 'State.' + id
    return render_template('9-states.html', states=states, id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
