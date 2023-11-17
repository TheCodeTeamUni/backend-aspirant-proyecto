from flask_restful import Resource
from flask import request
from datetime import datetime
from ..models import db, PersonalInformation, PersonalSchema, PersonalDetailSchema

personal_schema = PersonalSchema()
personal_detail_schema = PersonalDetailSchema()


class VistaPersonal(Resource):

    def post(self, idUser):
        # Crea la informacion personal del aspirante: /aspirant/personal/<int:idUser>

        try:
            personal = request.get_json()
            personal['idUser'] = idUser
            personal['birthdate'] = datetime.strptime(
                personal['birthdate'], '%d/%m/%Y')
            personal = PersonalInformation(**personal)

            # Save the information for the aspirant
            db.session.add(personal)
            db.session.commit()

            return personal_schema.dump(personal), 201

        except Exception as error:
            db.session.rollback()
            return {'error': 'A ocurrido un error'}, 400

    def get(self, idUser):
        # Retorna la informacion personal del aspirante: /aspirant/personal/<int:idUser>

        try:
            personal = PersonalInformation.query.filter_by(
                idUser=idUser).first()

            return personal_detail_schema.dump(personal), 200

        except Exception as error:
            return {'error': str(error)}, 400


class VistaPong(Resource):

    def get(self):
        # Retorna pong si el servicio se encuentra en linea: /
        return 'pong aspirantes V2.3', 200
