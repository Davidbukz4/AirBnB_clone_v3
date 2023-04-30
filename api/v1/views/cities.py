#!/usr/bin/python3
'''
Handles RESTful API for cities
'''
from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.city import City
from models.state import State


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def cities(state_id):
    ''' Returns list of an object in dict form '''
    li = []
    obj = storage.get(State, state_id)
    if obj:
        for item in obj.cities:
            li.append(item.to_dict())
        return jsonify(li)
    abort(404)


@app_views.route('/cities/<city_id>', methods=['GET', 'DELETE'],
                 strict_slashes=False)
def city_id(city_id):
    ''' Returns list of an object(city) with specific id in dict form '''
    obj = storage.get(City, city_id)
    if obj:
        if request.method == 'GET':
            return jsonify(obj.to_dict())
        elif request.method == 'DELETE':
            obj.delete()
            storage.save()
            return jsonify({}), 200
    abort(404)


@app_views.route('/states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def city_post(state_id):
    ''' adds a new object '''
    li = []
    obj = storage.get(State, state_id)
    if obj and obj.id == state_id:
        if not request.json:
            return jsonify("Not a JSON"), 400
        else:
            data = request.get_json()
            if 'name' not in data.keys():
                return jsonify("Missing name"), 400
            else:
                data["state_id"] = state_id
                new = City(**data)
                new.save()
                return jsonify(new.to_dict()), 201
    abort(404)


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def city_put(city_id):
    ''' updates an object '''
    obj = storage.get(City, city_id)
    if obj:
        if not request.json:
            return jsonify("Not a JSON"), 400
        else:
            data = request.get_json()
            unchanged = ['state_id', 'id', 'updated_at', 'created_at']
            for k, v in data.items():
                if k not in unchanged:
                    setattr(obj, k, v)
            storage.save()
            return jsonify(obj.to_dict())
    abort(404)
