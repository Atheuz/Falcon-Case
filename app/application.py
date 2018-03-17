from flask import Flask
from flask_restplus import Resource, Api, apidoc
from flask_restplus import reqparse
import json
from modules import api
from modules.models import db
from modules.models import cache

def create_app():
    app = Flask(__name__)
    prod = True
    if (prod):
        app.config.from_object('config.ProductionConfig')
    else:
        app.config.from_object('config.Config')

    db.init_app(app)
    api.init_app(app)
    db.create_all(app=app)
    cache.init_app(app, config={'CACHE_TYPE': app.config["CACHE_TYPE"]})

    return app