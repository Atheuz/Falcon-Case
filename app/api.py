from flask import Flask
from flask_restplus import Resource, Api, apidoc
from flask_restplus import reqparse
import json
from modules import api
from modules import db
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.SWAGGER_UI_LANGUAGES = ['en']
app.config.SWAGGER_UI_JSONEDITOR = True
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'

with open("db_config.json") as json_file:
    db_conf = json.load(json_file)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@localhost:5432/{}'.format(db_conf["username"], db_conf["password"], db_conf["database_name"])

db = SQLAlchemy(app)
api.init_app(app)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=80)