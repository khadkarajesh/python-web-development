import uuid

from extensions import db


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
        self.id = str(uuid.uuid4())
        self.degree = degree
        self.field_of_study = field_of_study
        self.start_date = start_date
        self.end_date = end_date
        self.institution = institution
        self.grade = grade
        self.description = description

    id = db.Column(db.String(), primary_key=True, unique=True, nullable=False)
    degree = db.Column(db.String(), nullable=False)
    field_of_study = db.Column(db.String(), nullable=False)
    start_date = db.Column(db.Date(), nullable=False)
    end_date = db.Column(db.Date(), nullable=False)
    institution = db.Column(db.String(), nullable=False)
    grade = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=False)
    employee_id = db.Column(db.String(), db.ForeignKey('employees.id'))
    employee = db.relationship('Employee', back_populates='educations')

    def to_dict(self):
        return {
            'id': self.id,
            'degree': self.degree,
            'field_of_study': self.field_of_study,
            'start_date': str(self.start_date),
            'end_date': str(self.end_date),
            'institution': self.institution,
            'grade': self.grade,
            'description': self.description
        }
