from flask_restful import Resource, marshal_with, reqparse, current_app, abort, marshal
from common.database import db
from sqlalchemy import exc
from models.natureza import NaturezaModel, natureza_campos

parser = reqparse.RequestParser()
parser.add_argument('tipo', required=True)

class NaturezasResource(Resource):
    # GET /naturezas
    @marshal_with(natureza_campos)
    def get(self):
        current_app.logger.info("Get - Naturezas")
        naturezas = NaturezaModel.query\
            .all()
        return naturezas, 200

class NaturezaResource(Resource):
    # GET /naturezas/<id>
    @marshal_with(natureza_campos)
    def get(self, natureza_id):
        current_app.logger.info("Get - Natureza: %s" % natureza_id)
        natureza = NaturezaModel.query.filter_by(id=natureza_id).first()
        if natureza is None:
            abort(404, message='Natureza {} nao existe'.format(natureza_id))

        return natureza, 200
