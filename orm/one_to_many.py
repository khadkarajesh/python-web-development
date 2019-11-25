from sqlalchemy import ForeignKey

import uuid

from extensions import db


class Employee(db.Model):
    __tablename__ = 'employees'

    def __init__(self,
                 name,
                 age,
                 gender,
                 phone):
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

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'gender': self.gender,
            'phone': self.phone
        }


class Education(db.Model):
    __tablename__ = 'educations'

    def __init__(self,
                 degree,
                 field_of_study,
                 start_date,
                 end_date,
                 institution,
                 grade,
                 description):
        self.degree = degree
        self.field_of_study = field_of_study
        self.start_date = start_date
        self.end_date = end_date
        self.institution = institution
        self.grade = grade
        self.description = description

    id = db.Column(db.String(), primary_key=True, unique=True, nullable=False, default=str(uuid.uuid4()))
    degree = db.Column(db.String(), nullable=False)
    field_of_study = db.Column(db.String(), nullable=False)
    start_date = db.Column(db.Date(), nullable=False)
    end_date = db.Column(db.Date(), nullable=False)
    institution = db.Column(db.String(), nullable=False)
    grade = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    employee_id = db.Column(db.String(), ForeignKey('employees.id'))
    employee = db.relationship('Employee', back_populates='educations')
