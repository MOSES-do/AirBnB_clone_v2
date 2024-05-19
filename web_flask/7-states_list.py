#!/usr/bin/python3
"""start a flask web application"""
from flask import Flask, render_template
from /AirBnB_clone_v2/models import storage, State
app = Flask(__name__)


@app.teardown_appcontext
def close_orm_session(exception):
    """remove current SQLAlchmey session"""
    storage.close()


@app('/states_list', strict_slashes=False)
def state_list():
    """render html page with state objects
        sorted by name
    """
    states = storage.all(State).values()
    sorted_states = sorted(states, key-lambda state: state.name)
    return render_template('7-states_list.html', states=sorted_states)


if __name__ = "__main__":
    app.run(host='0.0.0.0', port=5000)
