from flask_restx import Namespace, Resource, fields, marshal
from flask import request
from ..APImodels import candidate_model, promise_model, result_model
from ..DBmodels import Vote, Candidate, Promise, CandProm, Result
from flask import abort

vote_detail_ns = Namespace('vote_details', description='Vote details related operations')

@vote_detail_ns.route('/<int:vid>/candidate')
class Candidates(Resource):
    @vote_detail_ns.marshal_list_with(candidate_model)
    def get(self, vid):
        vote = Vote.query.get(vid)
        if not vote:
            abort(404, message="Vote not found")

        candidates = Candidate.query.filter_by(VID=vid).all()
        return candidates


@vote_detail_ns.route('/<int:vid>/<int:cid>')
class Promises(Resource):
    @vote_detail_ns.marshal_list_with(promise_model)
    def get(self, vid, cid):
        # 특정 후보자의 공약을 가져옴
        pid_objs = CandProm.query.filter_by(CID=cid).all()
        pids = [pid_obj.PID for pid_obj in pid_objs]
        
        if not pids:
            abort(404, message="No promises found for the candidate")        
        promises = Promise.query.filter(Promise.PID.in_(pids)).all()
        
        if not promises:
            abort(404, message="No promises found for the candidate") 
        
        # 공약의 내용을 반환
        return promises, 200

@vote_detail_ns.route('/<int:vid>/results')
class VoteResults(Resource):
    @vote_detail_ns.marshal_list_with(result_model)
    def get(self, vid):
        # 특정 투표(VID)에 대한 결과 조회
        results = Result.query.filter_by(VID=vid).all()
        if not results:
            abort(404, message="Results not found for the specified vote") 
        
        return [result for result in results], 200



