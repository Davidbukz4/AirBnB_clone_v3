#!/usr/bin/python3
'''
Handles RESTful API for states
'''
from models import storage
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.state import State


@app_views.route('/states/', methods=['GET'])
def states():
    ''' Returns list of an object in dict form '''
    li = []
    objs = storage.all('State')
    for item in objs:
        li.append(objs[item].to_dict())
    return jsonify(li)


@app_views.route('/states/<state_id>', methods=['GET', 'DELETE'])
def states_id(state_id):
    ''' Returns list of an object with specific id in dict form '''
    objs = storage.all('State')
    for item in objs:
        elem = objs[item].to_dict()
        if elem['id'] == state_id:
            if request.method == 'GET':
                return jsonify(elem)
            elif request.method == 'DELETE':
                objs[item].delete()
                storage.save()
                resp = {}
                return jsonify(resp)
    abort(404)


@app_views.route('/states/', methods=['POST'])
def states_post():
    ''' adds a new object '''
    if not request.json:
        return jsonify("Not a JSON"), 400
    else:
        data = request.get_json()
        if 'name' not in data.keys():
            return jsonify("Missing name"), 400
        else:
            new = State(**data)
            new.save()
            return jsonify(new.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def states_put(state_id):
    ''' updates an object '''
    objs = storage.all('State')
    for elem in objs:
        if objs[elem].id == state_id:
            if not request.json:
                return jsonify("Not a JSON"), 400
            else:
                data = request.get_json()
                unchanged = ['id', 'updated_at', 'created_at']
                for item in data:
                    if item not in unchanged:
                        setattr(objs[elem], item, data[item])
                objs[elem].save()
                return jsonify(objs[elem].to_dict())
    abort(404)
