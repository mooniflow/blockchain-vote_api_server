import os

class Config:
    DEBUG = True
    BASE_DIR = os.path.dirname(__file__)

    SQLALCHEMY_DATABASE_URI = 'mysql://admin:It12345!@47.128.242.146/voteDB'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

