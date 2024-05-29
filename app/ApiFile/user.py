from flask_restx import Namespace, Resource, fields, marshal
from flask import request
from ..APImodels import user_model, address_model, salt_model
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
class Users(Resource):
    @user_ns.marshal_list_with(user_model)
    def get(self, code):
        user = User.query.filter_by(Code=code).first()
        return user, 201


@user_ns.route('/<int:code>/address')
class UserAddressDetail(Resource):
    @user_ns.expect(address_model)
    @user_ns.marshal_with(address_model, code=201)
    def put(self, code):
        data = request.json
        user = User.query.filter_by(Code=code).first()

        if not user:
            api.abort(404, "User not found")

        user.Address = data['Address']
        db.session.commit()

        return user, 201

    def delete(self, code):
        user = User.query.filter_by(Code=code).first()

        if user:
            user.Address = None
            db.session.commit()
            return {'message': 'Address deleted successfully'}, 200
        else:
            return {'message': 'User not found'}, 404


@user_ns.route('/<int:code>/salt')
class UserSaltDetail(Resource):
    @user_ns.expect(salt_model)
    @user_ns.marshal_with(salt_model, code=201)
    def put(self, code):
        data = request.json
        user = User.query.filter_by(Code=code).first()

        if not user:
            api.abort(404, "User not found")

        user.Salt = data['Salt']
        db.session.commit()

        return user, 201

    def delete(self, code):
        user = User.query.filter_by(Code=code).first()

        if user:
            user.Salt = None
            db.session.commit()
            return {'message': 'Salt deleted successfully'}, 200
        else:
            return {'message': 'User not found'}, 404
