from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api

from api.add import add_api
from api.retrieve import retrieve_api

from gather import tasks
from gather import celery

from database import db
from database import cache

import sys

# DEV or PROD mode
# Default is DEV mode.
DEV = True
# If we have a second param to the script, then it's uwsgi and that means we are in production mode.
if (len(sys.argv) == 2):
    DEV = False

# Setup flask
app = Flask(__name__)
if (DEV == False):
    print("Loading in PROD mode")
    app.config.from_object('config.ProductionConfig')
else:
    print("Loading in DEV mode")
    app.config.from_object('config.Config')

# Set up API
api_instance = Api(doc='/api/',
                   version='v1.0',
                   title='falcon.io Case API',
                   description='This is the API for the falcon.io case.')

api_instance.add_namespace(add_api, path='/add')
api_instance.add_namespace(retrieve_api, path='/retrieve')
api_instance.init_app(app) # Initialize the api

# Set up celery with extra config
celery.conf['backend'] = app.config['CELERY_RESULT_BACKEND']
celery.conf['broker'] = app.config['CELERY_BROKER_URL']
celery.conf['accept_content'] = app.config['CELERY_ACCEPT_CONTENT']

TaskBase = celery.Task
class ContextTask(TaskBase):
    abstract = True
    def __call__(self, *args, **kwargs):
        with app.app_context():
            return TaskBase.__call__(self, *args, **kwargs)
celery.Task = ContextTask

# Set up database
db = SQLAlchemy()
db.init_app(app) # Initialize the database using the entries in the config set above.
db.drop_all(app=app) # Drop the table here, so we have a fresh start every time. In DEV mode we use a sqlite file, in PROD we use postgresql.
db.create_all(app=app) # If the database table doesn't already exist, then create it here. 

# Setup cache
cache.init_app(app, config={'CACHE_TYPE': app.config["CACHE_TYPE"]})

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=80)