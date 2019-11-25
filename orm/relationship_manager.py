from orm.one_to_many import Employee, Education
from extensions import db
import datetime


def create_user():
    employee = Employee('Bob Marley', '100', 'M', '24234')
    education = Education('Music',
                          'Bachelor Degree',
                          datetime.date.today(),
                          datetime.date.today(),
                          'Institute of Music',
                          'A',
                          'description')

    employee.educations.append(education)

    db.session.add(employee)
    db.session.commit()

    return employee


def add_education(user_id):
    employee = Employee.query.filter(Employee.id == user_id).first()

    education = Education('Science',
                          'Bachelor Degree in science',
                          datetime.date.today(),
                          datetime.date.today(),
                          'Institute of Science',
                          'A',
                          'description')

    employee.educations.append(education)
    db.session.commit()
    return employee


def remove_education(user_id, degree):
    employee = Employee.query.filter(Employee.id == user_id).first()
    for education in employee.educations:
        if education.degree == degree:
            employee.educations.remove(education)
            db.session.commit()
            return employee


def update_education(user_id, degree):
    employee = Employee.query.filter(Employee.id == user_id).first()
    for education in employee.educations:
        if education.degree == degree:
            education.institution = 'IOE'
            db.session.commit()


def get_employees():
    employees = Employee.query.all()
    for employee in employees:
        print(employee)


def get_educations():
    educations = Education.query.all()
    for education in educations:
        print(education.employee.name)
