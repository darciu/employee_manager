import sys
from modules.employees import Trainee, Junior, Mid, Senior, Administrative, Executive, Manager
from modules.database import DepartmentDatabase, EmployeeDatabase
from modules.excel_management import import_export_employees
from modules.search_employee import get_employee




def manage_menu():
    print("This module allows to add, modify or remove any employee from the database")
    condition = True
    while condition:
        print("""Please select one of the following options:
                1. Manage single employee (add or remove)
                2. Import or export employees (.xlsx or .xls)
                3. Back
                4. Exit application""")
        option = input()
        if option == "1":
            manage_single_menu()
        elif option == "2":
            import_export_employees()
        elif option == "3":
            condition = False
        elif option == "4":
            print("Goodbye")
            sys.exit()
        else:
            print("Provided value is not correct!")

def manage_single_menu():
    condition = True
    while condition:
        print("""Please select one of the following options:
                1. Add employee
                2. Remove employee
                3. Back
                4. Exit application""")
        option = input()
        if option == "1":

            add_single_employee()

        elif option == "2":

            remove_employee()

        elif option == "3":
            condition = False
        elif option == "4":
            print("Goodbye")
            sys.exit()
        else:
            print("Provided value is not correct!")


def add_single_employee():
    condition = True
    while condition:
        print("""Write down what position new employee is:
                Trainee, Junior, Mid, Senior, Administrative, Manager, Executive.

                If you want to back, press Enter...""")
        option = input()
        if option.lower() == "trainee":
            personal_data = get_personal_data_ver1()

            Trainee(personal_data[0], personal_data[1], personal_data[2], personal_data[3],
                    personal_data[4], personal_data[5]).add_to_database()


        elif option.lower() == "junior":
            personal_data = get_personal_data_ver1()

            Junior(personal_data[0], personal_data[1], personal_data[2], personal_data[3],
                   personal_data[4], personal_data[5]).add_to_database()

        elif option.lower() == "mid":
            personal_data = get_personal_data_ver1()

            Mid(personal_data[0], personal_data[1], personal_data[2], personal_data[3],
                personal_data[4], personal_data[5]).add_to_database()

        elif option.lower() == "senior":
            personal_data = get_personal_data_ver1()

            Senior(personal_data[0], personal_data[1], personal_data[2], personal_data[3],
                   personal_data[4], personal_data[5]).add_to_database()

        elif option.lower() == "administrative":
            personal_data = get_personal_data_ver2()

            Administrative(personal_data[0], personal_data[1], personal_data[2], personal_data[3],
                           personal_data[4]).add_to_database()



        elif option.lower() == "manager":
            personal_data = get_personal_data_ver1()

            Manager(personal_data[0], personal_data[1], personal_data[2], personal_data[3],
                    personal_data[4], personal_data[5]).add_to_database()


        elif option.lower() == "executive":
            personal_data = get_personal_data_ver2()

            Executive(personal_data[0], personal_data[1], personal_data[2], personal_data[3],
                      personal_data[4]).add_to_database()



        elif option == "":
            condition = False
        else:
            print("Invalid position name")


def remove_employee():
    row = get_employee()
    question = input("Do you really want to remove employee with ID {0}? ({1} {2}, year of birth {3}) (Y) ".format(row[0],row[1],row[2],row[4]))
    if question.upper() == "Y":
        db = EmployeeDatabase()
        db.remove_employee(row[0])




########################################



def get_personal_data_ver1():

    personal_data = list([get_name(),get_surname(),get_sex(),get_birth_year(),get_basic_salary(),get_department_id()])

    return personal_data



def get_personal_data_ver2():

    personal_data = list([get_name(),get_surname(),get_sex(),get_birth_year(),get_basic_salary()])

    return personal_data

def get_name():
    while True:
        name = input("Please provide name: ")
        if len(name) > 2:
            name = name[0].upper() + name[1:]
            name = name.strip()
            return name
        else:
            print("Name has to be at least three characters")

def get_surname():
    while True:
        name = input("Please provide surname: ")
        if len(name) > 2:
            name = name[0].upper() + name[1:]
            name = name.strip()
            return name
        else:
            print("Name has to be at least three characters")

def get_sex():
    while True:
        sex = input("Please provide sex (M/F): ")
        if sex.upper() == "M":
            return 1
        elif sex.upper() == "F":
            return 0
        else:
            print("Please provide correct value (M/F)!")

def get_birth_year():
    while True:
        birth_year = input("Please provide birth year: ")
        if birth_year.isnumeric():
            if int(birth_year) >= 1900 and int(birth_year) <= 2000:
                return birth_year
            else:
                print("Birth year must be a number between 1900 and 2000!")
        else:
            print("Birth year must be a number between 1900 and 2000!")

def get_basic_salary():
    while True:
        basic_salary = input("Please provide basic salary: ")
        if basic_salary.isnumeric():
            return basic_salary
        else:
            print("Basic salary has to be a number")


def get_department_id():
    db_dept = DepartmentDatabase()
    while True:
        dept_list = db_dept.return_dept_name_list()
        dept_name = input("Please provide department (if no department press Enter): ")
        if dept_name in dept_list:
            department_id = db_dept.get_department_id(dept_name)
            return department_id

        elif dept_name == "":
            return None
        else:
            print("Invalid value!")





