import sys
from database import DepartmentDatabase

def regexp_search():
    pass


def see_by_departments():

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




def search_menu():
    condition = True
    while condition:
        print("""Please select one of the following options:
                1. Search by first and last name
                2. See emplyees by departments
                3. Back
                4. Exit application""")
        option = input()
        if option == "1":
            regexp_search()
        elif option == "2":
            see_by_departments()
        elif option == "3":
            condition = False
        elif option == "4":
            print("Goodbye")
            sys.exit()
        else:
            print("Provided value is not correct!")


