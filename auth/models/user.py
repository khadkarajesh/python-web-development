from extensions import db
import uuid


class User(db.Model):
    id = db.Column(db.String(), primary_key=True, default=str(uuid.uuid4()))
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'profile': {
                'name': self.profile.name,
                'phone': self.profile.phone,
                'address': self.profile.address
            }
        }

    @classmethod
    def find_user_by(cls, email):
        return User.query.filter(User.email == email).first()

    @classmethod
    def find_user_by_id(cls, user_id):
        return User.query.filter(User.id == user_id).first()
