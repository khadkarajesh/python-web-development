import uuid

from extensions import db


class Profile(db.Model):

    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

    id = db.Column(db.String(), primary_key=True, default=str(uuid.uuid4()))
    name = db.Column(db.String())
    address = db.Column(db.String())
    phone = db.Column(db.String())
    user_id = db.Column(db.String(), db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('profile', uselist=False))
