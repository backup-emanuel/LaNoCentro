from flask_restful import Resource, marshal_with, reqparse, current_app, abort, marshal
from common.database import db
from sqlalchemy import exc
from models.cidade import CidadeModel, cidade_campos

parser = reqparse.RequestParser()
parser.add_argument('nome', required=True, help="Especifique um nome válido para a Cidade.")


class CidadesResource(Resource):
    # GET /cidades
    @marshal_with(cidade_campos)
    def get(self):
        current_app.logger.info("Get - Cidades")
        cidades = CidadeModel.query\
            .all()
        return cidades, 200

class CidadeResource(Resource):
    # GET /cidades/<id>
    @marshal_with(cidade_campos)
    def get(self, cidade_id):
        current_app.logger.info("Get - Cidade: %s" % cidade_id)
        cidade = CidadeModel.query.filter_by(id=cidade_id).first()
        if cidade is None:
            abort(404, message='Cidade {} nao existe'.format(cidade_id))

        return cidade, 200
