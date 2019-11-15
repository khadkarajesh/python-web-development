# -------------- Single Inheritance -------------------

# create class user
class User:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def login(self):
        print(F'Hi {self.name}')


user = User('Jon', 'USA')
print(user.name, user.address)


# Inherit from User

class Doctor(User):
    def __init__(self,
                 name,
                 address,
                 specialities,
                 schedule):
        super().__init__(name, address)
        self.specialities = specialities
        self.schedule = schedule

    def diagnose_patient(self, patient):
        print(F'diagnosed patient {patient.name} by doctor {self.name}')


class Patient(User):
    def __init__(self, name, address, diseases):
        super().__init__(name, address)
        self.diseases = diseases

    def get_appointment(self):
        print(F'{self.name} booked appointment')


patient = Patient('Jhon', 'KTM', 'Cough')
patient.get_appointment()

doctor = Doctor('Dr. Bob', 'KTM', 'OPD', 'SUN: 7-8')
doctor.diagnose_patient(patient)
