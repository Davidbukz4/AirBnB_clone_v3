#!/usr/bin/python3
"""
RESTful API
"""
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, abort
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)
app.url_map.strict_slashes = False


@app.errorhandler(404)
def invalid_page(err):
    ''' Returns a JSON-formatted 404 status code response '''
    resp = {"error": "Not found"}
    return jsonify(resp), 404


@app.teardown_appcontext
def teardown(exception=None):
    """ Tearsdown current session """
    storage.close()


if __name__ == '__main__':
    hosT = getenv('HBNB_API_HOST', default='0.0.0.0')
    porT = getenv('HBNB_API_PORT', default=5000)
    app.run(host=hosT, port=int(porT), threaded=True)
