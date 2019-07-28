import time
from database import EmployeeDatabase

class Employee:
    """Basic structure of employee"""

    def __init__(self, firstName, lastName, sex, birth_year, basic_salary, department_id = None, level = "A"):
        self.db = EmployeeDatabase()
        self.firstName = firstName
        self.lastName = lastName
        self.sex = sex
        self.birth_year = birth_year
        self.basic_salary = basic_salary
        self.level = level
        self.department_id = department_id


    def add_to_database(self):

        self.db.add_to_database(self.firstName, self.lastName, self.sex, self.birth_year, self.basic_salary, self.level, self.department_id, self.position)
        print("{0} {1} has been successfully added to database!\n\n".format(self.firstName, self.lastName))

class Trainee(Employee):
    def __init__(self, *args):
        super().__init__(*args)
        self.position = "Trainee"


class Junior(Employee):
    def __init__(self, *args):
        super().__init__(*args)
        self.position = "Junior"


class Mid(Employee):
    def __init__(self, *args):
        super().__init__(*args)
        self.level = "B"
        self.position = "Mid"

class Senior(Employee):
    def __init__(self, *args):
        super().__init__(*args)
        self.level = "C"
        self.position = "Senior"

class Administrative(Employee):
    def __init__(self, *args):
        super().__init__(*args)
        self.level = "B"
        self.position = "Administrative"


class Manager(Employee):
    def __init__(self, *args):
        super().__init__(*args)
        self.level = "D"
        self.position = "Manager"

class Executive(Manager, Administrative):
    def __init__(self, *args):
        super().__init__(*args)
        self.level = "E"
        self.position = "Manager"

