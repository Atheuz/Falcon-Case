from flask_restplus import Api
from .add import api as add_api
from .retrieve import api as retrieve_api
from .status import api as status_api

api = Api(doc='/api/',
          version='v1.0',
          title='falcon.io Case API',
          description='This is the API for the falcon.io case.')

api.add_namespace(status_api, path='/status')
api.add_namespace(add_api, path='/add')
api.add_namespace(retrieve_api, path='/retrieve')