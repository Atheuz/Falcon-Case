from flask import Flask
from flask_restplus import Resource, Api, apidoc
from flask_restplus import reqparse
import json
from modules import api

app = Flask(__name__)
app.config.SWAGGER_UI_LANGUAGES = ['en']
app.config.SWAGGER_UI_JSONEDITOR = True
app.config.SWAGGER_UI_DOC_EXPANSION = 'list'

api.init_app(app)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=80)