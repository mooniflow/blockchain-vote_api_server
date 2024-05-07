from flask_restx import Namespace, Resource, fields, marshal
from flask import request
from ..APImodels import user_model, vote_model, address_model
from ..DBmodels import User, Vote, Address
from flask import abort
from app import db

address_ns = Namespace('address', description='address related operations')

@address_ns.route('/')
class Addr(Resource):
    @address_ns.marshal_list_with(address_model)
    def get(self):
        addresses = Address.query.all()
        return [address for address in addresses]

@address_ns.route('/<int:uid>/<int:vid>')
class AddrDetail(Resource):
    @address_ns.expect(address_model)
    @address_ns.marshal_with(address_model, code=201)
    def post(self, uid, vid):
        new_address_data = request.json
        new_address = Address(
            UID=uid,
            VID=vid,
            Adr=new_address_data['Adr']
        )

        db.session.add(new_address)
        db.session.commit()

        # 추가된 주소 반환
        return new_address, 201

    def delete(self, uid, vid):
        # 데이터베이스에서 해당 주소를 찾기
        address = Address.query.filter_by(UID=uid, VID=vid).first()

        if address:
            # 주소가 존재하면 삭제하고 커밋
            db.session.delete(address)
            db.session.commit()
            return {'message': 'Address deleted successfully'}, 200
        else:
            # 주소가 존재하지 않으면 오류 메시지 반환
            return {'message': 'Address not found'}, 404
