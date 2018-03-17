from flask import Flask
from flask_restplus import Resource, Api, apidoc
from flask_restplus import reqparse
import json
from modules import api
from modules.models import db
from application import create_app
import sys

# Default is DEV mode.
DEV = True
# If we have a second param to the script, then it's uwsgi and that means we are in production mode.
if (len(sys.argv) == 2):
    DEV = False

app = create_app(DEV)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=80)