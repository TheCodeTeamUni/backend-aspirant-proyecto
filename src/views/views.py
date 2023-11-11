from datetime import datetime
from flask_restful import Resource
from flask import request
from ..models import db, PersonalInformation, PersonalDetailSchema, Education, EducationDetailSchema, \
    WorkExperience, WorkExperienceDetailSchema, Skill, SkillDetailSchema

personal_detail_schema = PersonalDetailSchema()
education_detail_schema = EducationDetailSchema()
work_experience_detail_schema = WorkExperienceDetailSchema()
skill_detail_schema = SkillDetailSchema()


class VistaBusquedaSkill(Resource):

    def get(self, Skill):
        # Retorna la información de un aspirante si tiene ciertas habilidades: /aspirant/<string:Skill>

        try:
            sql_query = "SELECT DISTINCT \
                p.idUser, name, lastName, skill, country, telephone, alterntiveEmail \
                FROM personal_information AS p \
                LEFT JOIN skill s ON s.idUser = p.idUser \
                WHERE s.skill  = :Skill"
            result = db.session.execute(sql_query, {'Skill': Skill})

            return [dict(row) for row in result], 200

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
