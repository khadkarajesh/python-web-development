from flask import request
from flask_restful import Resource

from orm.relationship_manager import create_user, add_education, get_employees


class OneToManyResource(Resource):

    @classmethod
    def get(cls):
        return get_employees()

    @classmethod
    def post(cls):
        user = create_user()
        educations = []
        for education in user.educations:
            data = {
                'field_of_study': education.field_of_study,
                'education': education.institution,
                'degree': education.degree
            }
            educations.append(data)
        return {
            'name': user.name,
            'educations': educations

        }

    @classmethod
    def put(cls):
        user = add_education(request.get_json()['id'])
        educations = []
        for education in user.educations:
            data = {
                'field_of_study': education.field_of_study,
                'education': education.institution,
                'degree': education.degree
            }
            educations.append(data)
        return {
            'name': user.name,
            'educations': educations

        }
