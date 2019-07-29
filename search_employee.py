import sys
from database import DepartmentDatabase
from employees import Trainee, Junior, Mid, Senior, Administrative, Executive, Manager

def emp_edit_personal_data(employee, id):
    condition = True
    while condition:
        print("""Please select one of the following options:
                1. Change first name
                2. Change last name
                3. Change basic salary
                4. Change position
                5. Change department
                6. Back""")

        option = input()

        if option == "1":
            employee.change_firstName(id)
        elif option == "2":
            employee.change_lastName(id)
        elif option == "3":
            employee.change_basic_salary(id)
        elif option == "4":
            employee.change_position(id)
        elif option == "5":
            employee.change_department(id)
        elif option == "6":
            condition = False
        else:
            print("Invalid value!")


def emp_personal_data_menu(employee, id):
    condition = True
    while condition:
        print("""Please select one of the following options:
                1. Display employee data
                2. Edit personal data
                3. Back""")
        option = input()
        if option == "1":
            employee.display_employee_data()
        elif option == "2":
            emp_edit_personal_data(employee, id)
        elif option == "3":
            condition = False
        else:
            print("Invalid value!")


def employee_menu(employee, id):
    condition = True
    while condition:
        print("""Please select one of the following options:
                1. Employee personal data
                2. Employee statistics 
                3. Special functions (according to employees position)
                4. Back
                5. Exit application""")

        option = input()
        if option == "1":
            emp_personal_data_menu(employee, id)
        elif option == "2":
            pass
        elif option == "3":
            pass
        elif option == "4":
            condition = False
        elif option == "5":
            sys.exit()
        else:
            print("Invalid value!")

    #staty to percentyl zarobków

def search_by_ID():
    """Create Employee instance according to the position"""
    row = get_employee()
    class_arguments = list([row[1],row[2],row[3],row[4],row[5],row[7]])
    emp_class_dictionary = {"Trainee":Trainee(*class_arguments),
                            "Junior":Junior(*class_arguments),
                            "Mid":Mid(*class_arguments),
                            "Senior":Senior(*class_arguments),
                            "Administrative":Administrative(*class_arguments),
                            "Manager":Manager(*class_arguments),
                            "Executive":Executive(*class_arguments)}

    employee = emp_class_dictionary.get(row[8])

    employee_menu(employee, row[0])

def see_by_department():

    db_dept = DepartmentDatabase()
    dept_list = db_dept.return_dept_name_list()
    dept_name = input("Please provide department (if no department press Enter): ")
    if dept_name in dept_list:
        department_id = db_dept.get_department_id(dept_name)
        db_dept.print_department_employees(department_id)
    elif dept_name == "":
        db_dept.print_department_employees(None)

    else:
        print("Invalid value!")

def see_by_position():

    db_dept = DepartmentDatabase()
    position_list = ['Trainee','Junior','Mid','Senior','Administrative','Manager','Executive']
    print('Available positions:\n')
    print(', '.join(position_list))
    print()
    position = input("Please provide position you want to display employees by: ")
    position = position.capitalize()
    if position in position_list:
        db_dept.print_position_employees(position)
    else:
        print("Invalid value...\n")





def search_menu():
    condition = True
    while condition:
        print("""Please select one of the following options:
                1. Search by Employee ID
                2. See employees by department
                3. See employees by position
                4. Back
                5. Exit application""")
        option = input()
        if option == "1":
            search_by_ID()
        elif option == "2":
            see_by_department()
        elif option == "3":
            see_by_position()
        elif option == "4":
            condition = False
        elif option == "5":
            print("Goodbye")
            sys.exit()
        else:
            print("Provided value is not correct!")


#######################

def get_employee():
    db = DepartmentDatabase()
    while True:
        ID = input("Please provide ID: ")
        if ID.isnumeric():
            row = db.check_ID(ID)
            if row != None:
                return row
            else:
                print("There is no such ID in database!\n")
        else:
            print("Invalid ID format!\n")