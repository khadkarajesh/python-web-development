from flask import Flask
from flask_restful import Api, Resource, request

app = Flask(__name__)
api = Api(app, prefix='/v1')


class HelloWorldResource(Resource):
    @classmethod
    def get(cls):
        return 'Congratulations you have successfully built first api in flask'


users = [{
    'name': 'Bob',
    'address': 'USA',
    'profession': 'software engineer'
},
    {
        'name': 'Jhon',
        'address': 'Australia',
        'profession': 'Architect'
    },
    {
        'name': 'Martin',
        'address': 'Canada',
        'profession': 'Singer'
    }
]


class UserResource(Resource):
    @classmethod
    def get(cls):
        return users

    @classmethod
    def post(cls):
        user = request.get_json()
        users.append(user)
        return user

    @classmethod
    def put(cls):
        data = request.get_json()
        name = data['name']
        for user in users:
            if user['name'] == name:
                users.remove(user)
                users.append(data)
        return data

    @classmethod
    def delete(cls):
        name = request.get_json()['name']
        for user in users:
            if user['name'] == name:
                users.remove(user)
                return {}, 204
        return {"message": F"User with {name} doesnt exit"}, 400


api.add_resource(UserResource, '/users')
api.add_resource(HelloWorldResource, '')

if __name__ == '__main__':
    app.run(debug=True)
