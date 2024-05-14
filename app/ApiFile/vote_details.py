from flask_restx import Namespace, Resource, fields, marshal
from flask import request
from ..APImodels import candidate_model, promise_model, result_model, canddetail_model
from ..DBmodels import Vote, Candidate, Promise, CandProm, Result, User
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
class CandDetails(Resource):
    @vote_detail_ns.marshal_with(canddetail_model)
    def get(self, vid, cid):
        cand = Candidate.query.get(cid)
        uid = cand.UID      
        user = User.query.get(uid)
        # 후보자 약력 리스트화
        profile_lists = cand.Profile.split('/')
        
        # 특정 후보자의 공약을 가져와 리스트화
        pid_objs = CandProm.query.filter_by(CID=cid).all()
        pids = [pid_obj.PID for pid_obj in pid_objs]
        
        if not pids:
            abort(404, message="No promises found for the candidate")        
        promises = Promise.query.filter(Promise.PID.in_(pids)).all()
        
        if not promises:
            abort(404, message="No promises found for the candidate") 
        
        content_lists = [promise.Content for promise in promises]

        return {
            'name': cand.Name,
            'department': user.Dep,
            'student_id': user.Code,
            'profile_lists': profile_lists,
            'content_lists': content_lists,
            'talk': cand.Talk
        }, 200

@vote_detail_ns.route('/<int:vid>/results')
class VoteResults(Resource):
    @vote_detail_ns.marshal_list_with(result_model)
    def get(self, vid):
        # 특정 투표(VID)에 대한 결과 조회
        results = Result.query.filter_by(VID=vid).all()
        if not results:
            abort(404, message="Results not found for the specified vote") 
        
        return [result for result in results], 200



