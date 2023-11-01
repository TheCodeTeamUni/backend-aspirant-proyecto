from flask_restful import Resource
from flask import request
from ..models import db, Skill, SkillSchema, SkillDetailSchema

skill_schema = SkillSchema()
skill_detail_schema = SkillDetailSchema()


class VistaSkill(Resource):

    def post(self, idUser):
        # Crea las habilidades del aspirante: /aspirant/skill/<int:idUser>

        try:
            skill = request.get_json()
            skill['idUser'] = idUser
            skill = Skill(**skill)

            db.session.add(skill)
            db.session.commit()

            return skill_schema.dump(skill), 201

        except Exception as error:
            db.session.rollback()
            return {'error': str(error)}, 400

    def get(self, idUser):
        # Retorna las habilidades del aspirante: /aspirant/skill/<int:idUser>

        try:
            skills = Skill.query.filter_by(idUser=idUser).all()

            return [skill_detail_schema.dump(al) for al in skills], 200

        except Exception as error:
            return {'error': str(error)}, 400
