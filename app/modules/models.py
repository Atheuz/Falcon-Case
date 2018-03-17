from sqlalchemy import Column, Integer, String, JSON
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

db = SQLAlchemy()
cache = Cache()

class JSONObject(db.Model):
    __tablename__ = 'json_table'
    json_id = Column(Integer, primary_key=True)
    json_contents = Column(String)

    def __init__(self, contents=None):
        self.json_contents = contents

    def __repr__(self):
        return '<JSONObject %r>' % (self.json_contents)