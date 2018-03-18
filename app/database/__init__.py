from flask_sqlalchemy import SQLAlchemy
import logging
from flask_caching import Cache

db = SQLAlchemy()
cache = Cache()