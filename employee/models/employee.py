import uuid

from extensions import db
from orm.company_employee_pivot import company_employee


class Employee(db.Model):
    __tablename__ = 'employees'

    def __init__(self,
                 name,
                 age,
                 gender,
                 phone):
        self.id = str(uuid.uuid4())
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

    id = db.Column(db.String(), primary_key=True, unique=True, nullable=False, default=str(uuid.uuid4()))
    name = db.Column(db.String(), nullable=False)
    age = db.Column(db.String(), nullable=False)
    gender = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String(), nullable=False)
    educations = db.relationship('Education', back_populates='employee')
    companies = db.relationship('Company', secondary=company_employee, back_populates='employees')

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'phone': self.phone
        }
