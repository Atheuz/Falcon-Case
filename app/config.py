class Config(object):
    """Dev mode config. Use sqlite file for the database and redis for the cache."""
    DEBUG = True
    DEVELOPMENT = True
    SWAGGER_UI_LANGUAGES = ['en']
    SWAGGER_UI_JSONEDITOR = True
    SWAGGER_UI_DOC_EXPANSION = 'list'
    PG_USERNAME = "postgres"
    PG_PASSWORD = "1234"
    PG_DATABASE = "postgres"
    PG_TABLE = "json_table"
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@localhost:5432/{}'.format(PG_USERNAME, PG_PASSWORD, PG_DATABASE)
    CACHE_TYPE = 'redis'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLOWER_PORT = "5555"
    FLOWER_BROKER_API = CELERY_BROKER_URL

class ProductionConfig(Config):
    """PROD mode config. Use postgresql for the database and redis for the cache."""
    DEVELOPMENT = False
    DEBUG = False
    CACHE_TYPE = 'redis'
    PG_USERNAME = "postgres"
    PG_PASSWORD = "1234"
    PG_DATABASE = "postgres"
    PG_TABLE = "json_table"
    SQLALCHEMY_DATABASE_URI = 'postgresql://{}:{}@db:5432/{}'.format(PG_USERNAME, PG_PASSWORD, PG_DATABASE)
    CELERY_BROKER_URL = 'redis://redis:6379'
    CELERY_RESULT_BACKEND = 'redis://redis:6379'