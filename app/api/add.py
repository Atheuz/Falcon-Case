from database import db
from database import cache
from database.models import JSONObject
from flask_restplus import Resource, Api, reqparse, Namespace, fields
from api import utils
from gather import tasks
import json

add_api = Namespace('add', description='Add new JSON objects to the store')

add = add_api.model('add', {
    's': fields.String(required=True, description='The JSON object to add to the store.'),
})

@add_api.route('/<s>')
@add_api.param('s', 'The JSON to add')
class AddAPI(Resource):    
    def get(self, s):
        """Add new JSON object to the store."""
        data = s
        
        if(data): # If we have an input we can proceed, otherwise it's a bad request.
            try: # Check if JSON is valid
                data_loaded = json.loads(data) 
            except json.decoder.JSONDecodeError as e: # If it's bad, then it's a bad request.
                return utils.bad_request_400("Bad input.")
        
            tasks.persist_to_db.delay(data_loaded)          
            cache.clear() # Invalidate cache, as the data in the cache no longer matches what is in the database.

            return utils.success_200(data) # Return success.
        else:
            return utils.bad_request_400("Missing input.")
        