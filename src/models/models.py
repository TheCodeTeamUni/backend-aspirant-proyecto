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
    createdAt = db.Column(db.DateTime, default=datetime.now())


class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idUser = db.Column(db.Integer, nullable=False)
    skill = db.Column(db.String(128))
    level = db.Column(db.Float)
    experience = db.Column(db.String(128))
    createdAt = db.Column(db.DateTime, default=datetime.now)


class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idUser = db.Column(db.Integer, nullable=False)
    typeEducation = db.Column(db.String(128))
    level = db.Column(db.String(128))
    title = db.Column(db.String(256))
    grade = db.Column(db.Boolean)
    institution = db.Column(db.String(256))
    startDate = db.Column(db.DateTime)
    endDate = db.Column(db.DateTime)
    createdAt = db.Column(db.DateTime, default=datetime.now)


class PersonalSchema(SQLAlchemySchema):
    class Meta:
        model = PersonalInformation
        load_instance = True

    id = fields.Integer()
    idUser = fields.Integer()
    createdAt = fields.DateTime()


class PersonalDetailSchema(SQLAlchemySchema):

    class Meta:
        model = PersonalInformation
        load_instance = True

    name = fields.String()
    lastName = fields.String()
    typeDocument = fields.String()
    document = fields.String()
    gender = fields.String()
    alterntiveEmail = fields.String()
    telephone = fields.String()
    country = fields.String()
    address = fields.String()
    birthdate = fields.DateTime()
    description = fields.String()
    photo = fields.String()


class PersonalDetailSchema2(SQLAlchemySchema):

    class Meta:
        model = PersonalInformation
        load_instance = True

    idUser = fields.Integer()
    name = fields.String()
    lastName = fields.String()
    country = fields.String()
    telephone = fields.String()
    alterntiveEmail = fields.String()
    photo = fields.String()


class WorkExperienceSchema(SQLAlchemySchema):
    class Meta:
        model = WorkExperience
        load_instance = True

    id = fields.Integer()
    idUser = fields.Integer()
    createdAt = fields.DateTime()


class WorkExperienceDetailSchema(SQLAlchemySchema):
    class Meta:
        model = WorkExperience
        load_instance = True

    company = fields.String()
    position = fields.String()
    actualJob = fields.Boolean()
    startDate = fields.DateTime()
    endDate = fields.DateTime()


class SkillSchema(SQLAlchemySchema):
    class Meta:
        model = Skill
        load_instance = True

    id = fields.Integer()
    idUser = fields.Integer()
    createdAt = fields.DateTime()


class SkillDetailSchema(SQLAlchemySchema):
    class Meta:
        model = Skill
        load_instance = True

    skill = fields.String()
    level = fields.Integer()
    experience = fields.String()


class EducationSchema(SQLAlchemySchema):
    class Meta:
        model = Education
        load_instance = True

    id = fields.Integer()
    idUser = fields.Integer()
    createdAt = fields.DateTime()


class EducationDetailSchema(SQLAlchemySchema):
    class Meta:
        model = Education
        load_instance = True

    typeEducation = fields.String()
    level = fields.String()
    title = fields.String()
    grade = fields.Boolean()
    institution = fields.String()
    startDate = fields.DateTime()
    endDate = fields.DateTime()
