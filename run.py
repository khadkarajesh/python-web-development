from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app, prefix='/v1')


class HelloWorldResource(Resource):
    @classmethod
    def get(cls):
        return 'Congratulations you have successfully built first api in flask'


api.add_resource(HelloWorldResource, '')

if __name__ == '__main__':
    app.run(debug=True)
