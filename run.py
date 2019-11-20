from flask import Flask
from flask_restful import Api, Resource, request
from flask_sqlalchemy import SQLAlchemy
import uuid

app = Flask(__name__)
api = Api(app, prefix='/v1')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://snc:csit@localhost/csit-snc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


class User(db.Model):
    id = db.Column(db.String(), primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String())


class HelloWorldResource(Resource):
    @classmethod
    def get(cls):
        return 'Congratulations you have successfully built first api in flask'


class UserResource(Resource):
    @classmethod
    def get(cls):
        db_users = User.query.all()
        response = []
        for db_user in db_users:
            user = {
                'id': db_user.id,
                'username': db_user.username,
                'password': db_user.password
            }
            response.append(user)
        return response

    @classmethod
    def post(cls):
        data = request.get_json()

        user = User()
        user.id = str(uuid.uuid4())

        user.username = data['username']
        user.password = data['password']

        db.session.add(user)
        db.session.commit()
        return {
            'id': user.id,
            'username': user.username,
            'password': user.password
        }

    @classmethod
    def put(cls):
        data = request.get_json()
        user_id = data['id']
        user = User.query.filter(User.id == user_id).first()
        if user:
            user.username = data['username']
            user.password = data['password']
            db.session.commit()
        return {
            'id': user.id,
            'name': user.username,
            'password': user.password
        }

    @classmethod
    def delete(cls):
        user_id = request.get_json()['id']
        user = User.query.filter(User.id == user_id).first()
        db.session.delete(user)
        db.session.commit()
        return {}, 204


api.add_resource(UserResource, '/users')
api.add_resource(HelloWorldResource, '')

if __name__ == '__main__':
    app.run(debug=True)
