from flask import Flask
from flask_restplus import Resource, Api, reqparse, Namespace, fields
import json
import utils

api = Namespace('retrieve', description='Retrieve all JSON objects in the store')

@api.route('/')
@api.doc()
class RetrieveAPI(Resource):
    """Retrieve all JSON objects in the store."""
    def get(self):
        store = [{"a":1, "b":2}, {"c":3}, {"d":4}]

        return utils.success_200(store)