from flask_restful import Resource
from flask import request
from datetime import datetime
from ..models import db, WorkExperience, WorkExperienceSchema

work_schema = WorkExperienceSchema()


class VistaWorkExperience(Resource):

    def post(self):
        # Crea la informacion personal del aspirante: /aspirant/work

        try:
            work = request.get_json()
            work['startDate'] = datetime.strptime(
                work['startDate'], '%d/%m/%Y')
            work['endDate'] = datetime.strptime(
                work['endDate'], '%d/%m/%Y')
            work = WorkExperience(**work)

            # Save the information for the aspirant
            db.session.add(work)
            db.session.commit()

            return work_schema.dump(work), 201

        except Exception as error:
            db.session.rollback()
            return {'error': str(error)}, 400
