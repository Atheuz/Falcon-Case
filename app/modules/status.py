from flask import Flask
from flask_restplus import Resource, Api, reqparse, Namespace, fields
import json
import utils

api = Namespace('status', description='Status page')

@api.route('/')
class StatusAPI(Resource):
    def get(self):
        """This returns the 'status' of the API, but given that the application must be running this can only ever be successful."""
        return utils.success_200("api is running")