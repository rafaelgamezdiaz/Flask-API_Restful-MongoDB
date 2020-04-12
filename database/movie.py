# Movie model
from .db import db


class Movie(db.Document):
    name = db.StringField(required=True, unique=True)
    year = db.IntField(required=False)
    cast = db.ListField(db.StringField(), required=True)
    genre = db.ListField(db.StringField(), required=True)