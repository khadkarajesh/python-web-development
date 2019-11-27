from flask import request
from flask_restful import Resource

from company.models.company import Company
from employee.models.employee import Employee
from extensions import db


class CompanyResource(Resource):
    @classmethod
    def get(cls, employee_id):
        employee = Employee.query.filter(Employee.id == employee_id).first()
        companies = []
        for company in employee.companies:
            companies.append({
                'name': company.name,
                'location': company.location
            })
        return companies

    @classmethod
    def post(cls, employee_id):
        employee = Employee.query.filter(Employee.id == employee_id).first()
        data = request.get_json()
        name = data['name']
        location = data['location']
        company = Company(name=name, location=location)
        employee.companies.append(company)
        db.session.commit()
        return {
            'name': company.name,
            'location': company.location
        }
