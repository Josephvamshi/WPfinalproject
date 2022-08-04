from datetime import datetime
from app import db


class Credentials(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password= db.Column(db.String(128))
    def __repr__(self):
        return '<Credentials {}>'.format(self.username)

class Studentdetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student=db.Column(db.String(64), index=True, unique=True)
    course= db.Column(db.String(64), index=True)
    fee= db.Column(db.String(128))
    city=db.Column(db.String(128))
    grades=db.Column(db.String(128))
    contact=db.Column(db.String(128))

    def __repr__(self):
        return '<Studentdetails{}>'.format(self.course)



