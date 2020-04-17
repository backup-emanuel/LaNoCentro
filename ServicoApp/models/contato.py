from common.database import db
from flask_restful import fields
from sqlalchemy.ext.orderinglist import ordering_list


contato_campos = {
    'id': fields.Integer(attribute='id'),
    'nome': fields.String(attribute='nome'),
    'email': fields.String(attribute='email'),
    'telefone': fields.String(attribute='telefone')
}


'''
    Classe Contato.
'''
class ContatoModel(db.Model):
    __tablename__ = 'tb_contato'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255))
    email = db.Column(db.String(255))
    telefone = db.Column(db.String(13))   
    
    def __init__(self, nome, email, telefone):
        self.nome = nome
        self.email = email
        self.telefone = telefone

    def __str__(self):
        return '<Contato %r>'%(self.nome)