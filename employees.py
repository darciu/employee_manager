import datetime
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

    def export_txt(self):
        n = datetime.datetime.now()
        f = open("output/{0}_{1}_export.txt".format(self.firstName, self.lastName), "w+")
        f.write("AUTOMATIC EMPLOYEE MANAGER EXPORT\n")
        f.write("FIRST NAME: {0}\n".format(self.firstName))
        f.write("LAST NAME: {0}\n".format(self.lastName))
        if self.sex == 0:
            f.write("SEX: FEMALE\n")
        elif self.sex == 1:
            f.write("SEX: MALE\n")
        f.write("SALARY: {0}\n".format(self.basic_salary))
        f.write("LEVEL: {0}\n\n".format(self.level))
        f.write("PRODUCED AT {0}-{1}-{2} {3}:{4}".format(n.year,n.month,n.day,n.hour,n.minute))


        f.close()

        print("File has been created!\n")

    def print_special_functions(self):
        condition = True
        while condition:
            print("""Choose from below special functions:
                    1. Export employee's information to text file
                    2. Increase basic salary per 100
                    3. Add a form of courtesy to the name (Mr/Mrs)
                    4. Back
                    5. Exit application""")
            option = input()

            if option == "1":

                question = input(
                    "Are you sure to export information for {0} {1}? (Y) ".format(self.firstName, self.lastName))

                if question.upper() == "Y":

                    self.export_txt()

            elif option == "2":
                pass
            elif option == "3":
                pass
            elif option == "4":
                condition = False
            elif option == "5":
                print("Goodbye!")
            else:
                print("Invalid value!")



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

    def print_special_functions(self):
        condition = True
        while condition:
            print("""Choose from below special functions:
                    1. Export employee's information to text file
                    2. Increase basic salary by 500
                    3. Double basic salary
                    4. Add a form of courtesy to the name (Sir/Madame)
                    5. Back
                    6. Exit application""")
            option = input()

            if option == "1":

                question = input(
                    "Are you sure to export information for {0} {1}? (Y) ".format(self.firstName, self.lastName))
                if question.upper() == "Y":

                    self.export_txt()

            elif option == "2":
                question = input("Are you sure to increase salary by 500? Current salary is {0} (Y)".format(self.basic_salary))
                if question.upper() == "Y":
                    pass
            elif option == "3":
                pass
            elif option == "4":
                pass
            elif option == "5":
                condition = False
            elif option == "6":
                print("Goodbye!")
            else:
                print("Invalid value!")

class Executive(Manager):
    def __init__(self, *args):
        super().__init__(*args)
        self.level = "E"
        self.position = "Executive"

