from flask import Flask
from flask_restplus import Resource, Api, apidoc
from flask_restplus import reqparse
import json
from modules import api
from modules.models import db
from modules.models import cache

def create_app():
    app = Flask(__name__)
    app.config.SWAGGER_UI_LANGUAGES = ['en']
    app.config.SWAGGER_UI_JSONEDITOR = True
    app.config.SWAGGER_UI_DOC_EXPANSION = 'list'

    with open("db_config.json") as json_file:
        db_conf = json.load(json_file)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{}:{}@db:5432/{}'.format(db_conf["username"], db_conf["password"], db_conf["database_name"])
        #app.config['SQLALCHEMY_DATABASE_URI'] = r'sqlite:///C:\Users\grave\Desktop\Falcon Case\test.db'

    db.init_app(app)
    api.init_app(app)
    cache.init_app(app)
    db.create_all(app=app)

    return app