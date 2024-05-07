from flask_restx import Namespace, Resource, fields, marshal
from flask import request
from ..APImodels import vote_model, candidate_model, promise_model
from ..DBmodels import Vote, Candidate, Promise, CandProm, VoteType, User
from datetime import datetime
from flask import abort

vote_ns = Namespace('vote', description='Vote related operations')


@vote_ns.route('/')
class Votes(Resource):
    @vote_ns.marshal_list_with(vote_model)
    def get(self):
        votes = Vote.query.all()
        return [marshal(vote, vote_model) for vote in votes]

@vote_ns.route('/past')
class PastVotes(Resource):
    @vote_ns.marshal_list_with(vote_model)
    def get(self):
        # 현재 시간
        current_time = datetime.now()
        # 투표 종료 시간이 현재 시간보다 이전인 투표만을 가져옴
        votes = Vote.query.filter(Vote.End < current_time).all()
        return [marshal(vote, vote_model) for vote in votes]

@vote_ns.route('/current')
class CurrentVotes(Resource):
    @vote_ns.marshal_list_with(vote_model)
    def get(self):
        # 현재 시간
        current_time = datetime.now()
        # 투표 시작 시간이 현재 시간보다 이전이고, 투표 종료 시간이 현재 시간 이후인 투표만을 가져옴
        votes = Vote.query.filter(Vote.Start < current_time, Vote.End > current_time).all()
        return [vote for vote in votes]

@vote_ns.route('/future')
class FutureVotes(Resource):
    @vote_ns.marshal_list_with(vote_model)
    def get(self):
        # 현재 시간
        current_time = datetime.now()
        # 투표 시작 시간이 현재 시간보다 이후인 투표만을 가져옴
        votes = Vote.query.filter(Vote.Start > current_time).all()
        return [vote for vote in votes]

@vote_ns.route('/<int:vid>')
class VoteDetail(Resource):
    @vote_ns.marshal_with(vote_model)
    def get(self, vid):
        vote = Vote.query.get(vid)
        if not vote:
            abort(404, message="Vote not found")
        return vote

@vote_ns.route('/<int:vid>/<int:code>')
class Verifying(Resource):
    def get(self, vid, code):
        vote = Vote.query.get(vid)
        if not vote:
            abort(404, message="Vote not found")
        vtype = vote.Type
        
        user = User.query.filter_by(Code=code).first()
        if not user:
            abort(404, message="User not found")

        alloweds = VoteType.query.filter_by(Vtype=vtype).all()
        if not alloweds:
            abort(404, message="Vote type not found")
        
        utype = user.UType
        for allowed in alloweds:
            if allowed.Utype == utype:
                return 1  # 유형이 허용되었음을 나타내는 값 반환
        
        return 0
