#!/usr/bin/python3
'''
Status module
'''

from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status')
def status_ok():
    ''' Returns status '''
    obj = {"status": "OK"}
    return jsonify(obj)


@app_views.route('/stats')
def status_all():
    ''' Returns the number of each object by type '''
    stat = {}
    stat['amenities'] = storage.count('Amenity')
    stat['cities'] = storage.count('City')
    stat['places'] = storage.count('Place')
    stat['reviews'] = storage.count('Review')
    stat['states'] = storage.count('State')
    stat['users'] = storage.count('User')
    return jsonify(stat)
