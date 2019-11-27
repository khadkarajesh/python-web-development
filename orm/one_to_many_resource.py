from flask import request
from flask_restful import Resource

from orm.relationship_manager import create_employee, add_education, get_employees, get_educations


class OneToManyResource(Resource):

    @classmethod
    def get(cls):
        get_educations()
        return get_employees()

    @classmethod
    def post(cls):
        data = request.get_json()
        user = create_employee(data)
        educations = []
        companies = []
        for education in user.educations:
            data = {
                'field_of_study': education.field_of_study,
                'education': education.institution,
                'degree': education.degree
            }
            educations.append(data)

        for company in user.companies:
            data = {
                'name': company.name,
                'location': company.location
            }
            companies.append(data)
        return {
            'name': user.name,
            'educations': educations,
            'companies': companies
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
