from flask_restx import Namespace, Resource, fields, marshal
from flask import request
from ..APImodels import user_model
from ..DBmodels import User
from app import db

user_ns = Namespace('user', description='User related operations')


@user_ns.route('/')
class Users(Resource):
    @user_ns.marshal_list_with(user_model)
    def get(self):
        users = User.query.all()
        return [user for user in users]

@user_ns.route('/<int:code>')
class UserDetail(Resource):
    @user_ns.expect(user_model)
    @user_ns.marshal_with(user_model, code=201)
    def put(self, code):
        Address_data = request.json
        user = User.query.filter_by(Code=code).first()
        user.Address = Address_data['Address']
        db.session.commit()

        return user, 201

    def delete(self, code):
        user = User.query.filter_by(Code=code).first()

        if user:
            user.Id = None
            db.session.commit()
            return {'message': 'Address deleted successfully'}, 200
        else:
            return {'message': 'Address not found'}, 404
