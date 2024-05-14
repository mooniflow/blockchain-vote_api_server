from app import db

class User(db.Model):
    UID = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Code = db.Column(db.Integer)
    Address = db.Column(db.String(300))
    Dep = db.Column(db.String(300))
    UType = db.Column(db.Integer)
 

class Candidate(db.Model):
    CID = db.Column(db.Integer, primary_key=True)
    VID = db.Column(db.Integer, db.ForeignKey('vote.VID'))
    UID = db.Column(db.Integer, db.ForeignKey('user.UID'))
    Name = db.Column(db.String(255))
    Img = db.Column(db.String(255))
    Profile = db.Column(db.Text)
    Talk = db.Column(db.Text)

class Promise(db.Model):
    PID = db.Column(db.Integer, primary_key=True)
    Content = db.Column(db.Text)

class CandProm(db.Model):
    CID = db.Column(db.Integer, db.ForeignKey('candidate.CID'), primary_key=True)
    PID = db.Column(db.Integer, db.ForeignKey('promise.PID'), primary_key=True)

class Result(db.Model):
    RID = db.Column(db.Integer, primary_key=True)
    VID = db.Column(db.Integer, db.ForeignKey('vote.VID'))
    CID = db.Column(db.Integer, db.ForeignKey('candidate.CID'))
    Ratio = db.Column(db.Float)

class Vote(db.Model):
    VID = db.Column(db.Integer, primary_key=True)
    Topic = db.Column(db.String(255))
    Start = db.Column(db.TIMESTAMP)
    End = db.Column(db.TIMESTAMP)
    State = db.Column(db.Integer)
    Type = db.Column(db.Integer)

class VoteType(db.Model):
    TID = db.Column(db.Integer, primary_key=True)
    Vtype = db.Column(db.Integer)
    Utype = db.Column(db.Integer)
