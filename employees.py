import time,datetime
from database import EmployeeDatabase, DepartmentDatabase

class Employee:
    """Basic structure of employee"""


    def __init__(self, firstName, lastName, sex, birth_year, basic_salary, department_id = None, level = "A"):

        self.db = EmployeeDatabase()
        self.db_dept = DepartmentDatabase()
        self.firstName = firstName
        self.lastName = lastName
        self.sex = sex
        self.birth_year = birth_year
        self.basic_salary = basic_salary
        self.level = level
        self.department_id = department_id
        self.now = datetime.datetime.now()

    def add_to_database(self):

        self.db.add_to_database(self.firstName, self.lastName, self.sex, self.birth_year, self.basic_salary, self.level, self.department_id, self.position)
        self.db.remove_employee_duplicates()
        print("{0} {1} has been successfully added to database!\n\n".format(self.firstName, self.lastName))

    def display_employee_data(self):

        print("First name: ", self.firstName)

        print("Last Name: ", self.lastName)

        if self.sex == 1:
            print("Sex: Male")
        elif self.sex == 0:
            print("Sex: Female")
        print("Age: ", int(self.now.year) - self.birth_year)

        print("Basic salary: ", self.basic_salary)

        print("Level: ", self.level)

        if self.department_id == None:
            print("Department: ", None)
        else:
            department_name = self.db_dept.get_department_name(self.department_id)
            print("Department: ", department_name)

        print("Positon: ",self.position)
        a = input("Press Enter to continue...\n")

    def change_firstName(self, id):

        from manage_employee import get_name
        print("Current name is: ", self.firstName)
        firstName = get_name()
        self.db.update_name(firstName, id)
        self.firstName = firstName

    def change_lastName(self, id):
        from manage_employee import get_surname
        print("Current name is: ", self.lastName)
        lastName = get_surname()
        self.db.update_surname(lastName, id)
        self.lastName = lastName

    def change_basic_salary(self,id):
        from manage_employee import get_basic_salary
        print("Current basic salary is: ", self.basic_salary)
        basic_salary = get_basic_salary()
        self.db.update_basic_salary(basic_salary, id)

    def change_position(self,id):
        print("Current basic salary is: ", self.position)
        position = self.get_position()
        self.db.update_basic_salary(position, id)


    def get_position(self):
        while True:
            position_list = ['Trainee','Junior','Mid','Senior','Administrative','Manager','Executive']
            print('Available positions:\n')
            print(', '.join(position_list))
            print()
            position = input("Please provide employees position: ")
            position = position.capitalize()
            if position in position_list:
                return position
            else:
                print("There is no such position!")

    def change_department(self, id):
        while True:
            if self.position in['Administrative','Executive']:
                print("This position has no department availbility")
                return
            else:
                if self.department_id == None:
                    print("Current department is: ", self.department_id)
                else:
                    print("Current department is: ", self.db_dept.get_department_name(self.department_id))

            dept_list =self.db_dept.return_dept_name_list()
            dept_name = input("Please provide department name from the list (For None write 'None'/To continue press Enter...)")
            if dept_name == "":
                return
            elif dept_name == "None":
                self.db.update_department_id(None,id)
            elif dept_name in dept_list:
                self.db.update_department_id(self.db_dept.get_department_id(dept_name),id)
                return
            else:
                print("Invalid value!\n")

    def min_salary(self):
        return self.db.get_min_salary()

    def max_salary(self):
        return self.db.get_max_salary()

    def average_salary(self):
        return self.db.get_average_salary()

    def sum_salary(self):
        return self.db.get_sum_salary()

    def count_salary(self):
        return self.db.get_count_salary()

    def count_lt_salary(self,basic_salary):
        return self.db.get_count_lt_salary(basic_salary)



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
        self.position = "Executive"

