from flask import Flask
from flask_restplus import Resource, Api, apidoc
from flask_restplus import reqparse
import json
from modules import api
from modules.models import db
from modules.models import cache

def create_app(dev_mode):
    """Setup the Flask application, the database, api and the cache.
       
       :param dev_mode: bool that determines whether or not the application is to be run in DEV mode or PROD mode.
    """

    app = Flask(__name__)
    if (dev_mode == False):
        print("Loading in PROD mode")
        app.config.from_object('config.ProductionConfig')
    else:
        print("Loading in DEV mode")
        app.config.from_object('config.Config')

    db.init_app(app) # Initialize the database using the entries in the config set above.
    api.init_app(app) # Initialize the api
    db.drop_all(app=app) # Drop the table here, so we have a fresh start every time. In DEV mode we use a sqlite file, in PROD we use postgresql.
    db.create_all(app=app) # If the database table doesn't already exist, then create it here. 
    cache.init_app(app, config={'CACHE_TYPE': app.config["CACHE_TYPE"]}) # Initialize the cache, if in DEV mode we use simple cache, in PROD we use redis.

    return app