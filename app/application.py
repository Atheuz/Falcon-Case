from flask import Flask
from flask_restplus import Resource, Api, apidoc
from flask_restplus import reqparse
from celery import Celery
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
import json
from gather.add import add_api
from gather.retrieve import retrieve_api

class ContextHolder(object):
    def __init__(self):
        app = None
        celery = None
        db = None
        api = None
        cache = None

    def make_db(self):
        # Set up the database
        self.db = SQLAlchemy()
        self.db.init_app(self.app) # Initialize the database using the entries in the config set above.
        self.db.drop_all(app=self.app) # Drop the table here, so we have a fresh start every time. In DEV mode we use a sqlite file, in PROD we use postgresql.
        self.db.create_all(app=self.app) # If the database table doesn't already exist, then create it here. 

    def make_api(self):
        # Set up API and register the API namespaces.
        self.api = Api(doc='/api/',
                  version='v1.0',
                  title='falcon.io Case API',
                  description='This is the API for the falcon.io case.')

        self.api.add_namespace(add_api, path='/add')
        self.api.add_namespace(retrieve_api, path='/retrieve')
        self.api.init_app(self.app) # Initialize the api

    def make_cache(self):
        # Set up the cache.
        self.cache = Cache()
        self.cache.init_app(self.app, config={'CACHE_TYPE': self.app.config["CACHE_TYPE"]})

    def make_celery(self):
        # Set up celery
        self.celery = Celery(self.app.import_name, backend=self.app.config['CELERY_RESULT_BACKEND'],
                        broker=self.app.config['CELERY_BROKER_URL'])
        self.celery.conf['accept_content'] = self.app.config['CELERY_ACCEPT_CONTENT']
        TaskBase = self.celery.Task
        class ContextTask(TaskBase):
            abstract = True
            def __call__(self, *args, **kwargs):
                with self.app.app_context():
                    return TaskBase.__call__(self, *args, **kwargs)
        self.celery.Task = ContextTask

    def create_app(self, dev_mode):
        """Setup the Flask application, the database, api and the cache.
           
           :param dev_mode: bool that determines whether or not the application is to be run in DEV mode or PROD mode.
        """

        self.app = Flask(__name__)
        if (dev_mode == False):
            print("Loading in PROD mode")
            self.app.config.from_object('config.ProductionConfig')
        else:
            print("Loading in DEV mode")
            self.app.config.from_object('config.Config')

        #self.make_celery() # Initialize celery for dispatching objects to database.
        #self.make_db()
        #self.make_api()
        #self.make_cache()