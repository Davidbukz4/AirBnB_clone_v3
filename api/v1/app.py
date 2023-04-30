#!/usr/bin/python3
"""
RESTful API
"""
from models import storage
from api.v1.views import app_views
from flask import Flask
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(exception=None):
    """ Tearsdown current session """
    storage.close()


if __name__ == '__main__':
    hosT = getenv('HBNB_API_HOST')
    porT = getenv('HBNB_API_PORT')
    app.run(host=hosT, port=porT, threaded=True)
