from flask import Flask
from flask_restplus import Resource, Api, reqparse, Namespace, fields
import json
import utils
from models import JSONObject
from api import db

api = Namespace('retrieve', description='Retrieve all JSON objects in the store')

@api.route('/')
@api.doc()
class RetrieveAPI(Resource):
    """Retrieve all JSON objects in the store."""
    def get(self):
        store = JSONObject.query.all()
        
        return utils.success_200([(x.json_id, x.json_contents) for x in store])