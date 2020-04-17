import os

# Autenticação
secret_key = 'ifpbinfo'

# Conexões com os Bancos de dados.
usuario = 'root' #os.environ.get('DB_USUARIO', 'db_senha')
senha = 'ifpbinfo' #os.environ.get('DB_SENHA', 'db_senha')

# Depuração
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{}:{}@localhost/{}?charset=utf8&use_unicode=1'.format(
    usuario,
    senha,
    'lanocentro'
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_BINDS = {}
