import time
from database import EmployeeDatabase

class Employee:
    """Basic structure of employee"""

    def __init__(self, firstName, lastName, sex, birth_year, basic_salary, level="A"):
        self.db = EmployeeDatabase()
        self.firstName = firstName
        self.lastName = lastName
        self.sex = sex
        self.birth_year = birth_year
        self.basic_salary = basic_salary
        self.level = level

    def add_to_database(self):
        self.db.add_to_database(self.firstName, self.lastName, self.sex, self.birth_year, self.basic_salary, self.level)
        print("{0} {1} has been successfully added to database!\n\n".format(self.firstName, self.lastName))

class Trainee(Employee):
    def __init__(self, *args):
        super().__init__(*args)


class Junior(Employee):
    pass

class Mid(Employee):
    pass

class Senior(Employee):
    pass

class Administrative(Employee):
    pass

class Manager(Employee):
    pass

class Executive(Manager, Administrative):
    pass

