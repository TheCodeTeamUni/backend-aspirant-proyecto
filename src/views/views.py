from datetime import datetime
from flask_restful import Resource
from flask import request
from ..models import db, PersonalInformation, PersonalDetailSchema, Education, EducationDetailSchema, \
    WorkExperience, WorkExperienceDetailSchema, Skill, SkillDetailSchema, PersonalDetailSchema2

personal_detail_schema_search = PersonalDetailSchema2()
personal_detail_schema = PersonalDetailSchema()
education_detail_schema = EducationDetailSchema()
work_experience_detail_schema = WorkExperienceDetailSchema()
skill_detail_schema = SkillDetailSchema()


class VistaBusquedaSkill(Resource):

    def get(self, Skill_search):
        # Retorna la información de un aspirante si tiene ciertas habilidades: /aspirant/<string:Skill>

        try:

            query = db.session.query(PersonalInformation, Skill).join(
                Skill, PersonalInformation.idUser == Skill.idUser).filter(Skill.skill == Skill_search).all()

            data = []

            for row in query:
                personal = personal_detail_schema_search.dump(row[0])
                skill = skill_detail_schema.dump(row[1])

                data_aspirante = {
                    "idUser": personal['idUser'],
                    "name": personal['name'],
                    "lastName": personal['lastName'],
                    "skill": skill['skill'],
                    "level": skill['level'],
                    "country": personal['country'],
                    "telephone": personal['telephone'],
                    "alterntiveEmail": personal['alterntiveEmail'],
                    "photo": personal['photo']
                }

                data.append(data_aspirante)

            return data, 200

        except Exception as error:
            return {'error': str(error)}, 400


class VistaBusquedaAspirante(Resource):

    def get(self, idUser):
        # Retorna la información de un aspirante: /aspirant/<int:idUser>

        try:
            # Get personal information
            personal = PersonalInformation.query.filter_by(
                idUser=idUser).first()

            personal_detail = personal_detail_schema.dump(personal)

            # Get education information
            educations = Education.query.filter_by(idUser=idUser).all()

            education_detail = [
                education_detail_schema.dump(al) for al in educations]

            # Get work experience information
            work_experiences = WorkExperience.query.filter_by(
                idUser=idUser).all()

            work_experience_detail = [
                work_experience_detail_schema.dump(al) for al in work_experiences]

            # Get skill information
            skills = Skill.query.filter_by(idUser=idUser).all()

            skill_detail = [skill_detail_schema.dump(al) for al in skills]

            data = {
                "personal_information": personal_detail,
                "education": education_detail,
                "work_experience": work_experience_detail,
                "skill": skill_detail
            }

            return data, 200

        except Exception as error:
            return {'error': str(error)}, 400
