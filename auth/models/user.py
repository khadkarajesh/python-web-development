from extensions import db
import uuid


class User(db.Model):
    id = db.Column(db.String(), primary_key=True, default=str(uuid.uuid4()))
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

    @classmethod
    def find_user_by(cls, email):
        return User.query.filter(User.email == email).first()
