from src import create_app
from flask_cors import CORS
from flask_restful import Api
from flask_jwt_extended import JWTManager
from src.models import db
from src.views import VistaPong, VistaPersonal
from src.views import VistaWorkExperience
from src.views import VistaSkill
from src.views import VistaEducation
from src.views import VistaBusquedaAspirante, VistaBusquedaSkill, VistaAspirantes

application = create_app('default')
app_context = application.app_context()
app_context.push()

db.init_app(application)
db.create_all()

cors = CORS(application)

api = Api(application)
api.add_resource(VistaWorkExperience, '/aspirant/work/<int:idUser>')
api.add_resource(VistaEducation, '/aspirant/education/<int:idUser>')
api.add_resource(VistaPersonal, '/aspirant/personal/<int:idUser>')
api.add_resource(VistaSkill, '/aspirant/skill/<int:idUser>')
api.add_resource(VistaPong, '/')

api.add_resource(VistaBusquedaAspirante, '/aspirant/<int:idUser>')
api.add_resource(VistaBusquedaSkill, '/aspirant/<string:Skill_search>')
api.add_resource(VistaAspirantes, '/aspirant')

jwt = JWTManager(application)


@application.errorhandler(404)
def page_not_found(e):
    return 'Pagina no encontrada', 404


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=3002, debug=True)
