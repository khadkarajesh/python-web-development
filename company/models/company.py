import uuid

from extensions import db
from orm.company_employee_pivot import company_employee


class Company(db.Model):
    __tablename__ = 'companies'

    def __init__(self, name, location):
        self.id = str(uuid.uuid4())
        self.name = name
        self.location = location

    id = db.Column(db.String(), primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String())
    location = db.Column(db.String())
    employees = db.relationship('Employee', secondary=company_employee, back_populates='companies')
