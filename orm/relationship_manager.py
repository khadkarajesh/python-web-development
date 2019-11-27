from company.models.company import Company
from education.models.education import Education
from employee.models.employee import Employee
from extensions import db
import datetime


def create_employee(data):
    name = data['name']
    age = data['age']
    gender = data['gender']
    phone = data['phone']

    # degree = data['education']['degree']
    # field_of_study = data['education']['field_of_study']
    # start_date = data['education']['start_date']
    # end_date = data['education']['end_date']
    # institution = data['education']['institution']
    # grade = data['education']['grade']
    # description = data['education']['description']
    #
    # company_name = data['company']['name']
    # company_location = data['company']['location']
    #
    employee = Employee(name, age, gender, phone)
    # education = Education(degree,
    #                       field_of_study,
    #                       start_date,
    #                       end_date,
    #                       institution,
    #                       grade,
    #                       description)
    #
    # employee.educations.append(education)
    #
    # company = Company(company_name, company_location)
    # employee.companies.append(company)

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
