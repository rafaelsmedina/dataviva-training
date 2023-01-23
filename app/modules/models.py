from app import db
from datetime import date
from hashlib import md5

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        about_me = db.Column(db.String(140))
        last_seen = db.Column(db.DateTime, default=date.today())
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=date.today())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)