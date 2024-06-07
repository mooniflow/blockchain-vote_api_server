from flask import Flask
from flask_restx import Api
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
    
CORS(app)

# SQLAlchemy 초기화
db = SQLAlchemy()
db.init_app(app)
migrate = Migrate()
migrate.init_app(app, db)

# Flask-RestX API 초기화
api = Api(app)
    
# API 네임스페이스 추가
from app.ApiFile.user import user_ns
from app.ApiFile.vote import vote_ns
from app.ApiFile.vote_details import vote_detail_ns

api.add_namespace(user_ns)
api.add_namespace(vote_ns)
api.add_namespace(vote_detail_ns)


