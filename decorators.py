from functools import wraps
from flask import Flask, request
from flask_restful import Resource, Api


def authorize(func):
    @wraps(func)
    def authorize_user(*args, **kwargs):
        print('executed before login')
        if request.headers.get('Authorization', None) is not None:
            return func(*args, **kwargs)
        else:
            print('user should be authorize')

    print('executed after')
    return authorize_user


def doctor(func):
    @wraps(func)
    def is_doctor(*args, **kwargs):
        if request.headers.get('Role', None) == 'doctor':
            return func(*args, **kwargs)
        else:
            print('user must be doctor')

    return is_doctor


@doctor
@authorize
def login():
    print('hey login')


class LoginResource(Resource):
    @authorize
    def post(self):
        return 'success'


app = Flask(__name__)
api = Api(app)
api.add_resource(LoginResource, '/auth/login')

if __name__ == '__main__':
    app.run()
