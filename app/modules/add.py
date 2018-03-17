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
    def get(self, s):
        """Add new JSON object to the store."""
        data = s
        
        if(data): # If we have an input we can proceed, otherwise it's a bad request.
            try: # Check if JSON is valid
                data_loaded = json.loads(data) 
            except json.decoder.JSONDecodeError as e: # If it's bad, then it's a bad request.
                return utils.bad_request_400("Bad input.")
        
            obj = JSONObject(contents=data_loaded) # Load into sqlalchemy object defined.
            db.session.add(obj)
            db.session.commit() # Add and commit it to the session.
            
            cache.clear() # Invalidate cache, as the data in the cache no longer matches what is in the database.

            return utils.success_200(data) # Return success.
        else:
            return utils.bad_request_400("Missing input.")
        