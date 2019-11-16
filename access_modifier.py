class Doctor:
    def __init__(self,
                 name,
                 address,
                 specialities,
                 schedule,
                 degree):
        self.name = name
        self.address = address
        self.specialities = specialities
        self.schedule = schedule
        self.__degree = degree

    def __diagnose_patient(self):
        print(F'diagnosed patient bob by doctor {self.name}')


if __name__ == '__main__':
    doctor = Doctor('Dr. Bob', 'KTM', 'OPD', 'SUN: 7-8', 'MBBS')
    # can get method name as
    print(dir(Doctor))

    # Output of print
    # ['_Doctor__diagnose_patient',
    # '__class__',
    # '__delattr__',
    # '__dict__',
    # '__dir__',
    # '__doc__',
    # '__eq__',
    # '__format__',
    # '__ge__',
    # '__getattribute__',
    # '__gt__',
    # '__hash__',
    # '__init__',
    # '__init_subclass__',
    # '__le__',
    # '__lt__',
    # '__module__',
    # '__ne__',
    # '__new__',
    # '__reduce__',
    # '__reduce_ex__',
    # '__repr__',
    # '__setattr__',
    # '__sizeof__',
    # '__str__',
    # '__subclasshook__',
    # '__weakref__',
    # 'login']

    doctor._Doctor__diagnose_patient()
