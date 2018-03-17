from sqlalchemy import Column, Integer, String, JSON
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache

db = SQLAlchemy() # TODO: Move to settings.py?
cache = Cache() # TODO: Move to settings.py?

class JSONObject(db.Model):
    """Definition of the JSON schema to be used by SQLAlchemy"""

    __tablename__ = 'json_table'
    json_id = Column(Integer, primary_key=True)
    json_contents = Column(String) # TODO: Fix this, we want to store JSON, not String.

    def __init__(self, contents=None):
        self.json_contents = contents

    def __repr__(self):
        return '<JSONObject %r>' % (self.json_contents)