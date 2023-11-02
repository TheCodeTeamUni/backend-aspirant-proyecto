from datetime import datetime
from flask_restful import Resource
from flask import request
from ..models import db, Education, EducationSchema, EducationDetailSchema

education_schema = EducationSchema()
education_detail_schema = EducationDetailSchema()


class VistaEducation(Resource):

    def post(self, idUser):
        # Crea la informacion academica del aspirante: /aspirant/education/<int:idUser>

        try:
            education = request.get_json()
            education['idUser'] = idUser
            education['startDate'] = datetime.strptime(
                education['startDate'], '%d/%m/%Y')
            if education['grade'] == True:
                education['endDate'] = datetime.strptime(
                    education['endDate'], '%d/%m/%Y')
            education = Education(**education)

            db.session.add(education)
            db.session.commit()

            return education_schema.dump(education), 201

        except Exception as error:
            db.session.rollback()
            return {'error': str(error)}, 400

    def get(self, idUser):
        # Retorna a informacion academica del aspirante: /aspirant/education/<int:idUser>

        try:
            educations = Education.query.filter_by(idUser=idUser).all()

            return [education_detail_schema.dump(al) for al in educations], 200

        except Exception as error:
            return {'error': str(error)}, 400
