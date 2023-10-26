import uuid
from flask_restful import Resource
from flask import request
from datetime import datetime, timedelta
from flask_jwt_extended import create_access_token, decode_token
from ..models import db, PersonalInformation, PersonalSchema
from ..utils import encrypt

personal_schema = PersonalSchema()


class VistaPersonal(Resource):

    def post(self):
        # Crea la informacion personal del aspirante: /aspirant/personal

        try:
            personal = request.get_json()
            personal['birthdate'] = datetime.strptime(
                personal['birthdate'], '%d/%m/%Y')
            personal = PersonalInformation(**personal)

            # Save the information for the aspirant
            db.session.add(personal)
            db.session.commit()

            return personal_schema.dump(personal), 201

        except Exception as error:
            db.session.rollback()
            return {'error': str(error)}, 400


class VistaPong(Resource):

    def get(self):
        # Retorna pong si el servicio se encuentra en linea: /
        return 'pong users', 200
