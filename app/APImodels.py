from flask_restx import fields
from app import api

# User 모델 정의
user_model = api.model('User', {
    'UID': fields.Integer(required=False, description='UID, auto_increment'),
    'Code': fields.Integer(required=True, description='student identification number'),
    'Address': fields.String(required=True, description='kernel address account'),
    'Dep': fields.String(required=False, ddescription='Department'),
    'UType': fields.Integer(required=False, ddescription='User type')
})


# Candidate 모델 정의
candidate_model = api.model('Candidate', {
    'CID': fields.Integer(required=True, description='Candidate ID'),
    'VID': fields.Integer(description='Vote ID')
})

# CandDetail 모델 정의
canddetail_model = api.model('CandDetails', {
    'name': fields.String,
    'department': fields.String,
    'student_id': fields.Integer,
    'img_url': fields.String,
    'profile_lists': fields.List(fields.String),
    'content_lists': fields.List(fields.String),
    'talk': fields.String
})
# Promise 모델 정의
promise_model = api.model('Promise', {
    'PID': fields.Integer(required=True, description='Promise ID'),
    'Content': fields.List(fields.String, description='Promise Content')
})

# CandProm 모델 정의
candprom_model = api.model('CandProm', {
    'CID': fields.Integer(description='Candidate ID'),
    'PID': fields.Integer(description='Promise ID')
})

# Result 모델 정의
result_model = api.model('Result', {
    'RID': fields.Integer(description='Result ID'),
    'VID': fields.Integer(required=True, description='Vote ID'),
    'CID': fields.Integer(description='Candidate ID'),
    'Ratio': fields.Float(description='Result Ratio')
})

# Vote 모델 정의
vote_model = api.model('Vote', {
    'VID': fields.Integer(required=True, description='Vote ID'),
    'Topic': fields.String(description='Vote Topic'),
    'Start': fields.DateTime(description='Vote Start Time'),
    'End': fields.DateTime(description='Vote End Time'),
    'State': fields.Integer(description="Vote state"), 
    'Type': fields.Integer(description='Vote Type ID')
})

# VoteType 모델 정의
votetype_model = api.model('VoteType', {
    'TID': fields.Integer(description='Vote Type ID'),
    'Utype': fields.Integer(description='Vote Type')
})
