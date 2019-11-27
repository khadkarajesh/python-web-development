from sqlalchemy import ForeignKey

import uuid

from extensions import db

company_employee = db.Table('company_employee_association',
                            db.Column('company_id', db.String(), db.ForeignKey('companies.id'), primary_key=True),
                            db.Column('employee_id', db.String(), db.ForeignKey('employees.id'), primary_key=True))
