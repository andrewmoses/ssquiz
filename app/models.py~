from app import db
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    pwdhash = db.Column(db.String(54))
    email = db.Column(db.String(120), index=True, unique=True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, username,email, password):
	self.username = username.title()
	self.email = email.lower()
	self.set_password(password)
     
    def set_password(self, password):
	self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
	
	return check_password_hash(self.pwdhash, password)

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_title = db.Column(db.String(140))
    job_lastdate = db.Column(db.String(64))
    job_vaccancies = db.Column(db.Integer)
    job_lookingfor = db.Column(db.String(64))
    job_ctc = db.Column(db.String(64))
    job_contract = db.Column(db.String(14))
    job_workingdays = db.Column(db.Integer)
    job_refer = db.Column(db.String(14))
    job_desc = db.Column(db.String(140))
    job_skills = db.Column(db.String(140))
    job_company = db.Column(db.String(64))

    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.job_title)
