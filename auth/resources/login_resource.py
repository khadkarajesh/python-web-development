from flask import request
from flask_restful import Resource

from auth.manager import login


class LoginResource(Resource):
    @classmethod
    def post(cls):
        data = request.get_json()
        return login(data['email'], data['password'])
