from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
import os
import pandas as pd
import numpy as np
import json
import html

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('js', type=str, help='Dummy JSON to store.')

class DummyAPI(Resource):
    def get(self):
        try:
            args = parser.parse_args()
            data = args['js']
            # Put on db.

            return {"Message": data}, 200
        except Exception as e:
            raise e
            return {"Message": "Bad get input!"}, 400

if __name__ == '__main__':
    api.add_resource(DummyAPI, '/add')
    app.run(host='127.0.0.1', debug=True, port=80)