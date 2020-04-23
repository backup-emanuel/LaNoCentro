from common.database import db
from flask_restful import fields
from sqlalchemy.ext.orderinglist import ordering_list


natureza_campos = {
    'id': fields.Integer(attribute='id'),
    'tipo': fields.String(attribute='tipo')
}


'''
    Classe Natureza da empresa.
'''
class NaturezaModel(db.Model):
    __tablename__ = 'tb_natureza'

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(255))

    def __init__(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return '<Natureza %s>'%(self.tipo)
