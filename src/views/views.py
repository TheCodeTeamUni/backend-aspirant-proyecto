import uuid
from flask_restful import Resource
from flask import request
from datetime import datetime, timedelta
from flask_jwt_extended import create_access_token, decode_token
from ..models import db, PersonalInformation, PersonalSchema
from ..utils import encrypt

personal_schema = PersonalSchema()

class VistaPong(Resource):

    def get(self):
        # Retorna pong si el servicio se encuentra en linea: /
        return 'pong users', 200
