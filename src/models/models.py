from marshmallow_sqlalchemy import SQLAlchemySchema
from marshmallow import fields
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class PersonalInformation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idUser = db.Column(db.Integer, nullable=False, unique=True)
    name = db.Column(db.String(50))
    lastName = db.Column(db.String(128))
    typeDocument = db.Column(db.String(20))
    document = db.Column(db.String(50))
    gender = db.Column(db.String(10))
    alterntiveEmail = db.Column(db.String(128))
    telephone = db.Column(db.String(50))
    country = db.Column(db.String(50))
    address = db.Column(db.String(128))
    birthdate = db.Column(db.DateTime)
    description = db.Column(db.String)
    photo = db.Column(db.String)
    createdAt = db.Column(db.DateTime, default=datetime.now())


class WorkExperience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idUser = db.Column(db.Integer, nullable=False)
    company = db.Column(db.String(128))
    position = db.Column(db.String(128))
    actualJob = db.Column(db.Boolean)
    startDate = db.Column(db.DateTime)
    endDate = db.Column(db.DateTime)
    description = db.Column(db.String)
    createdAt = db.Column(db.DateTime, default=datetime.now())


class PersonalSchema(SQLAlchemySchema):
    class Meta:
        model = PersonalInformation
        load_instance = True

    id = fields.Integer()
    idUser = fields.Integer()
    createdAt = fields.DateTime()


class WorkExperienceSchema(SQLAlchemySchema):
    class Meta:
        model = WorkExperience
        load_instance = True

    id = fields.Integer()
    idUser = fields.Integer()
    createdAt = fields.DateTime()
