from app import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(40), index = True)
    desc = db.Column(db.String(200), index = True) 

    def __repr__(self):
        return '<Name %r>' % (self.name)
