from flask import request
from flask_restful import Resource
from ..manager import create_user


class SignupResource(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        return create_user(data['email'], data['password'])
