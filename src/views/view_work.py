from flask_restful import Resource
from flask import request
from datetime import datetime
from ..models import db, WorkExperience, WorkExperienceSchema, WorkExperienceDetailSchema

work_schema = WorkExperienceSchema()
work_detail_schema = WorkExperienceDetailSchema()

class VistaWorkExperience(Resource):

    def post(self, idUser):
        # Crea la información laboral del aspirante: /aspirant/work/<int:idUser>

        try:
            work = request.get_json()
            work['idUser'] = idUser
            work['startDate'] = datetime.strptime(
                work['startDate'], '%d/%m/%Y')

            if work['actualJob'] == False:
                work['endDate'] = datetime.strptime(
                    work['endDate'], '%d/%m/%Y')
            work = WorkExperience(**work)

            db.session.add(work)
            db.session.commit()

            return work_schema.dump(work), 201

        except Exception as error:
            db.session.rollback()
            return {'error': str(error)}, 400
        
    def get(self, idUser):
        # Retorna la información laboral del aspirante: /aspirant/work/<int:idUser>

        try:
            works = WorkExperience.query.filter_by(idUser=idUser).all()

            return [work_detail_schema.dump(al) for al in works], 200

        except Exception as error:
            return {'error': str(error)}, 400
