from flask_restful import Resource
from flask import request
from datetime import datetime
from ..models import db, Skill, SkillSchema

skill_schema = SkillSchema()


class VistaSkill(Resource):

    def post(self):
        # Crea las habilidades del aspirante: /aspirant/skill

        try:
            skill = request.get_json()
            skill = Skill(**skill)

            # Save the information for the aspirant
            db.session.add(skill)
            db.session.commit()

            return skill_schema.dump(skill), 201

        except Exception as error:
            db.session.rollback()
            return {'error': str(error)}, 400
