import os

class Config:
    DEBUG = True
    BASE_DIR = os.path.dirname(__file__)

    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

