from flask_restplus import Api
from .add import api as add_api
from .retrieve import api as retrieve_api
from .index import api as index_api

api = Api(doc='/api/',
          version='v1.0',
          title='falcon.io Case API',
          description='This is the API for the falcon.io case.')

api.add_namespace(index_api, path='/index')
api.add_namespace(add_api, path='/add')
api.add_namespace(retrieve_api, path='/retrieve')