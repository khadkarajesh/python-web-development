from flask import request
from flask_restful import Resource

from employee.models.employee import Employee
from orm.relationship_manager import create_employee


class EmployeeResource(Resource):

    @classmethod
    def post(cls):
        employee = create_employee(request.get_json())
        return employee.to_dict()

    @classmethod
    def put(cls):
        pass

    @classmethod
    def delete(cls):
        pass

    @classmethod
    def get(cls):
        employees = Employee.query.all()
        data = []
        for employee in employees:
            data.append({
                'id': employee.id,
                'name': employee.name
            })
        return data
