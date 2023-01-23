from hashlib import md5

class User(UserMixin, db.Model):
    
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        about_me = db.Column(db.String(140))
        last_seen = db.Column(db.DateTime, default=datetime.utcnow)
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)