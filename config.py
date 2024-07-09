import os

SECRET_KEY = 'Mithrandir'

SQLALCHEMY_DATABASE_URI = \
  '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'mysql+mysqlconnector',
    usuario = 'root',
    senha = 'allb0109.asetimo7',
    servidor = 'localhost',
    database = 'jogoteca'
  )
  
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'