from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property
from config import bcrypt

from config import db

class Fisherperson(db.Model, SerializerMixin):
    __tablename__ = 'fisherpersons'

    id = 