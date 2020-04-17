from flask import Flask, Blueprint
from flask_restful import Api
from flask_cors import CORS
from common.settings import *
from common.logging import *
from resources.endereco import *
from resources.contato import *
from resources.empresa import *

app = Flask(__name__)

# Settings
app.config['DEBUG'] = DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = SQLALCHEMY_TRACK_MODIFICATIONS
app.config['SQLALCHEMY_BINDS'] = SQLALCHEMY_BINDS

# Configure logging
handler = logging.FileHandler(LOGGING_LOCATION)
handler.setLevel(LOGGING_LEVEL)
formatter = logging.Formatter(LOGGING_FORMAT)
handler.setFormatter(formatter)
app.logger.addHandler(handler)

db.init_app(app)

api_bp = Blueprint('api', __name__)
api = Api(api_bp, prefix='/lanocentro/api')

# Recursos
api.add_resource(EnderecosResource, '/enderecos')
api.add_resource(EnderecoResource, '/enderecos/<endereco_id>')

api.add_resource(ContatosResource, '/contatos')
api.add_resource(ContatoResource, '/contatos/<contato_id>')

api.add_resource(EmpresasResource, '/empresas')

# Blueprints para Restful.
app.register_blueprint(api_bp)

# CORS - requisição multi-clients
cors = CORS(app, resources={r"/lanocentro/api/*": {"origins": "*"}})

if __name__ == '__main__':
    app.run(threaded=True)
