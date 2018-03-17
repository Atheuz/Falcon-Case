from flask import Flask
from flask_restplus import Resource, Api, reqparse, Namespace, fields
import json
import utils
from .models import JSONObject
from .models import cache

api = Namespace('retrieve', description='Retrieve JSON objects from the store.')

retrieve = api.model('retrieve', {
    'id': fields.Integer(required=True, description='The document to retrieve.'),
})

@api.route('/<id>')
@api.param('id', 'The id of the JSON object that we want to retrieve.')
class RetrieveAPI(Resource):
    @api.doc("Retrieve the JSON object matching the id from the store.")
    @cache.memoize(50)
    def get(self, id):
        """Retrieve the JSON object matching the id from the store."""
        object = JSONObject.query.get(id)

        if(object): # If we successfully retrieved an object given the identifier, then return success and the object.
            return utils.success_200((object.json_id, object.json_contents))
        else: # Otherwise the object could not be found, so return an error.
            return utils.bad_request_400("Could not find object with id: {}".format(id))

@api.route('/')
class RetrieveListAPI(Resource):
    @api.doc("Retrieve all JSON objects in the store.")
    @cache.cached(50)
    def get(self):
        """Retrieve all JSON objects in the store."""
        store = JSONObject.query.all()
        
        return utils.success_200([(x.json_id, x.json_contents) for x in store])