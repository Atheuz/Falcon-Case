from flask import Flask
from flask_restplus import Resource, Api, reqparse, Namespace, fields
import json
import utils

api = Namespace('index', description='Index page')

@api.route('/')
class IndexAPI(Resource):
    """Index page."""
    def get(self):
        return utils.success_200("api is running")