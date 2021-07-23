from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100))
    email = db.Column(db.String(200))
    phone = db.Column(db.String(15))
    gender = db.Column(db.String(6))
    password = db.Column(db.String(200))

    def __repr__(self):
        return '<User id {}, name {}>'.format(self.id, self.username)
