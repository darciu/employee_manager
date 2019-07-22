
from database import EmployeeDatabase

class Employee:
    """Basic structure of employee"""

    def __init__(self, firstName, lastName, sex, date_of_birth, basic_salary, level="A"):
        self.db = EmployeeDatabase()
        self.firstName = firstName
        self.lastName = lastName
        self.sex = sex
        self.date_of_birth = date_of_birth
        self.basic_salary = basic_salary
        self.level = level

    def add_to_database(self):
        self.db.add_to_database(self.firstName, self.lastName, self.sex, self.date_of_birth, self.basic_salary, self.level)

class Trainee(Employee):
    def __init__(self):
        super().__init__()


class Junior:
    pass

class Mid:
    pass

class Senior:
    pass

class Administrative:
    pass

class Manager:
    pass

class Executive(Manager, Administrative):
    pass

