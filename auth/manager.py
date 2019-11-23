import bcrypt

from extensions import db
from auth.models.user import User


def create_user(email, password):
    user = User.find_user_by(email)

    if user:
        return {'message': F'user already exist with email {email}'}, 409

    user = User()
    user.password = hash_password(password)
    user.email = email

    db.session.add(user)
    db.session.commit()

    return {
        "email": user.email,
        "id": user.id
    }


def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')


def match_password(password, hashed_password):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))


def login(email, password):
    user = User.find_user_by(email)

    if user is None:
        return {'message': 'invalid username/password'}, 401

    if user.email == email and match_password(password, user.password):
        return {
            'id': user.id,
            'email': user.email
        }
    return {'message': 'invalid username/password'}, 401
