from enum import unique
import os
import datetime
from sqlalchemy import Column, String, Integer, Boolean, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = 'bootcamp'

database_path = "postgresql://{}:{}@{}/{}".format(
    "postgres", "abc", "localhost:5432", database_name
)

db = SQLAlchemy()

"""
setup_db(app)
    binds a flask application and a SQLAlchemy service
"""


def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


"""
Users

"""


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    public_key = db.Column(db.Integer, unique=True, nullable=False)

    def insert(self):
        db.session.add(self)
        db.session.commit()


"""
CodingSchool

"""


class CodingSchool(db.Model):
    __tablename__ = 'coding_schools'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    state = Column(String, nullable=False)
    address = Column(String, nullable=False)
    rating = Column(Integer)

    def __init__(self, name, state, address, rating):
        self.name = name
        self.state = state
        self.address = address
        self.rating = rating

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'name': self.name,
            'state': self.state,
            'address': self.address,
            'rating': self.rating
        }
