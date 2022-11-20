# здесь модель SQLAlchemy для сущности, также могут быть дополнительные методы работы с моделью (но не с базой,
# с базой мы работает в классе DAO)
from marshmallow import Schema, fields
from setup_db import db


class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class DirectorSchema(Schema):
    id = fields.Int()
    name = fields.Str()
