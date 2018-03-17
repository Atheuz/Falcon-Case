class Config(object):
    DEBUG = True
    DEVELOPMENT = True
    SWAGGER_UI_LANGUAGES = ['en']
    SWAGGER_UI_JSONEDITOR = True
    SWAGGER_UI_DOC_EXPANSION = 'list'
    SQLALCHEMY_DATABASE_URI = r'sqlite:///.\test.db'
    CACHE_TYPE = 'simple'

class ProductionConfig(Config):
    DEVELOPMENT = False
    DEBUG = False
    PG_USERNAME = "postgres"
    PG_PASSWORD = "1234"
    PG_DATABASE = "postgres"
    PG_TABLE = "json_table"
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@db:5432/{}'.format(PG_USERNAME, PG_PASSWORD, PG_DATABASE)
    CACHE_TYPE = 'redis'