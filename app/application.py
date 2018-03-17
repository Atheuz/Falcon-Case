from flask import Flask
from flask_restplus import Resource, Api, apidoc
from flask_restplus import reqparse
import json
from modules import api
from modules.models import db
from modules.models import cache

def create_app(dev_mode):
    app = Flask(__name__)
    if (dev_mode == False):
        print("Loading in PROD mode")
        app.config.from_object('config.ProductionConfig')
    else:
        print("Loading in DEV mode")
        app.config.from_object('config.Config')

    db.init_app(app)
    api.init_app(app)
    db.create_all(app=app)
    cache.init_app(app, config={'CACHE_TYPE': app.config["CACHE_TYPE"]})

    return app