from flask_restful import Resource, marshal_with, reqparse, current_app, abort, marshal
from common.database import db
from sqlalchemy import exc
from models.estado import EstadoModel, estado_campos

parser = reqparse.RequestParser()
parser.add_argument('nome', required=True, help="Especifique um nome válido para o Estado.")

class EstadosResource(Resource):
    # GET /estados
    @marshal_with(estado_campos)
    def get(self):
        current_app.logger.info("Get - Estados")
        estados = EstadoModel.query\
            .all()
        return estados, 200

class EstadoResource(Resource):
    # GET /estados/<id>
    @marshal_with(estado_campos)
    def get(self, estado_id):
        current_app.logger.info("Get - Estado: %s" % estado_id)
        estado = EstadoModel.query.filter_by(id=estado_id).first()
        if estado is None:
            abort(404, message='Estado {} nao existe'.format(estado_id))

        return estado, 200
