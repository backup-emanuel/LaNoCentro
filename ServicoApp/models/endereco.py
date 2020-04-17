from common.database import db
from flask_restful import fields
from sqlalchemy.ext.orderinglist import ordering_list


endereco_campos = {
    'id': fields.Integer(attribute='id'),
    'logradouro': fields.String(attribute='logradouro'),
    'numero': fields.String(attribute='numero'),
    'complemento': fields.String(attribute='complemento'),
    'cidade': fields.String(attribute='cidade'),
    'estado': fields.String(attribute='estado'),
    'cep': fields.String(attribute='cep'),
    'ponto_referencia': fields.String(attribute='ponto_referencia'),
}


'''
    Classe Endereço.
'''
class EnderecoModel(db.Model):
    __tablename__ = 'tb_endereco'

    id = db.Column(db.Integer, primary_key=True)
    logradouro = db.Column(db.String(255))
    numero = db.Column(db.String(4))
    complemento = db.Column(db.String(45))
    cidade = db.Column(db.String(45))
    estado = db.Column(db.String(45))
    cep = db.Column(db.String(8))
    ponto_referencia = db.Column(db.String(65))
    
    def __init__(self, logradouro, numero, complemento, cidade, estado, cep, ponto_referencia):
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.ponto_referencia = ponto_referencia

    def __str__(self):
        return '<Endereco %s>'%(self.logradouro)