from flask import request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from auth.manager import add_user_profile


class UserProfile(Resource):

    @classmethod
    @jwt_required
    def post(cls, user_id):
        data = request.get_json()
        return add_user_profile(user_id, data)
