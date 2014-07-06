from app import db, app
from werkzeug.security import generate_password_hash, check_password_hash
import flask.ext.whooshalchemy as whooshalchemy

class Job(db.Model):
    __searchable__ = ['name', 'desc']
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40), index = True)
    desc = db.Column(db.String(200), index = True) 
    completed = db.Column(db.Boolean, default=False)
    date = db.Column(db.DateTime)
    building = db.Column(db.String(15))
    room = db.Column(db.String(5))
    type = db.Column(db.String(15)) 

    def __repr__(self):
        return '<Name %r>' % (self.name)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), index = True)
    password = db.Column(db.String(20), index = True)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)

whooshalchemy.whoosh_index(app, Job)
