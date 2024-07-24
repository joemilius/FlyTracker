from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from config import bcrypt

from config import db

class Fisherperson(db.Model, SerializerMixin):
    __tablename__ = 'fisherpersons'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.Sting)
    lastname = db.Column(db.String)
    username = db.Column(db.String)
    state = db.Column(db.String)