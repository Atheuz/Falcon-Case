from flask import Flask
from flask_restplus import Resource, Api, reqparse, Namespace, fields
import json
import utils
from .models import JSONObject
from .models import db
from .models import cache

api = Namespace('add', description='Add new JSON objects to the store')

add = api.model('add', {
    's': fields.String(required=True, description='The JSON object to add to the store.'),
})

@api.route('/<s>')
@api.param('s', 'The JSON to add')
class AddAPI(Resource):
    """Add new JSON object to the store"""
    
    def get(self, s):
        data = s

        # Check if JSON is valid
        if(data):
            try:
                data_loaded = json.loads(data)
            except json.decoder.JSONDecodeError as e:
                return utils.bad_request_400("Bad input.")
        
            obj = JSONObject(contents=data_loaded)
            db.session.add(obj)
            db.session.commit()
            # Invalidate cache.
            cache.clear()
            return utils.success_200(data)
        else:
            return utils.bad_request_400("Missing input.")
        