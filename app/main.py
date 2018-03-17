from flask import Flask
from flask_restplus import Resource, Api, apidoc
from flask_restplus import reqparse
import json
from modules import api
from modules.models import db
from application import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=80)