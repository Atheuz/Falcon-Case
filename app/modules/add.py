from flask import Flask
from flask_restplus import Resource, Api, reqparse, Namespace, fields
import json
import utils

api = Namespace('add', description='Add new JSON objects to the store')

add = api.model('add', {
    'json': fields.String(required=True, description='The JSON to add'),
})

@api.route('/')
@api.param('json', 'The JSON to add')
@api.doc(params={'json': 'The JSON to add'})
class AddAPI(Resource):
    """Add new JSON object to the store"""
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('json', type=str, help='Dummy data to store, JSON format.')    
        args = parser.parse_args(strict=True)

        data = args['json']

        # Check if JSON is valid
        if(data):
            try:
                data = json.loads(data)
                data = json.dumps(data)
            except json.decoder.JSONDecodeError as e:
                return utils.bad_request_400("Bad input.")
        
            return utils.success_200(data)
        
        else:
            return utils.bad_request_400("Missing input.")
        