from common.database import db
from flask_restful import fields
from sqlalchemy.ext.orderinglist import ordering_list


estado_campos = {
    'id': fields.Integer(attribute='id'),
    'nome': fields.String(attribute='nome')
}


'''
    Classe Estado.
'''
class EstadoModel(db.Model):
    __tablename__ = 'tb_estado'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return '<Estado %s>'%(self.nome)
