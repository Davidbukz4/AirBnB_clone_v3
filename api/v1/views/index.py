#!/usr/bin/python3
'''
Status module
'''

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status')
def status_ok():
    ''' Returns status '''
    obj = {"status": "OK"}
    return jsonify(obj)
