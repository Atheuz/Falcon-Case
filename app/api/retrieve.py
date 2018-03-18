from database import db
from database import cache
from database.models import JSONObject
from flask_restplus import Resource, Api, reqparse, Namespace, fields
from api import utils
import json

retrieve_api = Namespace('retrieve', description='Retrieve JSON objects from the store.')

retrieve = retrieve_api.model('retrieve', {
    'id': fields.Integer(required=True, description='The document to retrieve.'),
})

@retrieve_api.route('/<id>')
@retrieve_api.param('id', 'The id of the JSON object that we want to retrieve.')
class RetrieveAPI(Resource):
    @retrieve_api.doc("Retrieve the JSON object matching the id from the store.")
    @cache.memoize(60)
    def get(self, id):
        """Retrieve the JSON object matching the id from the store."""
        object = JSONObject.query.get(id)

        if(object): # If we successfully retrieved an object given the identifier, then return success and the object.
            return utils.success_200((object.json_id, object.json_contents))
        else: # Otherwise the object could not be found, so return an error.
            return utils.bad_request_400("Could not find object with id: {}".format(id))

@retrieve_api.route('/')
class RetrieveListAPI(Resource):
    @retrieve_api.doc("Retrieve all JSON objects in the store.")
    @cache.cached(60)
    def get(self):
        """Retrieve all JSON objects in the store."""
        store = JSONObject.query.all()
        
        return utils.success_200([(x.json_id, x.json_contents) for x in store])