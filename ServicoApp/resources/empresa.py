from flask_restful import Resource, marshal_with, reqparse, current_app, abort, marshal
from common.database import db
from sqlalchemy import exc
from models.empresa import EmpresaModel, empresa_campos
from models.endereco import EnderecoModel

parser = reqparse.RequestParser()
parser.add_argument('nome', required=True)
parser.add_argument('natureza', required=True)
parser.add_argument('endereco', type=dict)
parser.add_argument('email', required=True)
parser.add_argument('telefone', required=True)
parser.add_argument('instagram', required=False)
parser.add_argument('facebook', required=False)


class EmpresasResource(Resource):
    # GET /empresas
    @marshal_with(empresa_campos)
    def get(self):
        current_app.logger.info("Get - Empresas")
        empresas = EmpresaModel.query\
            .all()
        return empresas, 200

    # POST /empresas
    def post(self):
        current_app.logger.info("Post - Empresa")
        try:
            # Parser JSON
            args = parser.parse_args()
            current_app.logger.info("Empresa: %s:" % (args))

            # args
            nome = args['nome']
            natureza = args['natureza']            
            endereco_id = args['endereco']['id']
            email = args['email']
            telefone = args['telefone']
            instagram = args['instagram']
            facebook = args['facebook']            

            # Recovering existing resources
            endereco = EnderecoModel.query.filter_by(id=endereco_id).first()

            empresa = EmpresaModel(nome, natureza, endereco, email, telefone, instagram, facebook)

            # Criação da Empresa.
            db.session.add(empresa)
            db.session.commit()

        except exc.SQLAlchemyError:
            current_app.logger.error("Exceção")
            return 404

        return marshal(empresa, empresa_campos), 201