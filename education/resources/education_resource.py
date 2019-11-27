from flask import request
from flask_restful import Resource

from education.models.education import Education
from employee.models.employee import Employee
from extensions import db


class EducationResource(Resource):
    @classmethod
    def get(cls, employee_id):
        employee = Employee.query.filter(Employee.id == employee_id).first()
        educations = []
        for education in employee.educations:
            data = {
                'field_of_study': education.field_of_study,
                'education': education.institution,
                'degree': education.degree
            }
            educations.append(data)
        return educations

    @classmethod
    def post(cls, employee_id):
        employee = Employee.query.filter(Employee.id == employee_id).first()
        data = request.get_json()
        degree = data['degree']
        field_of_study = data['field_of_study']
        start_date = data['start_date']
        end_date = data['end_date']
        institution = data['institution']
        grade = data['grade']
        description = data['description']

        education = Education(degree,
                              field_of_study,
                              start_date,
                              end_date,
                              institution,
                              grade,
                              description)

        employee.educations.append(education)
        db.session.commit()

        return education.to_dict()
