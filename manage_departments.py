import sys
from database import DepartmentDatabase


def manage_dept_menu():
    condition = True
    db_dept = DepartmentDatabase()
    while condition:
        print("""Please select one of the following options:
                1. Add new depatment
                2. Edit department name
                3. Remove department
                4. Back
                5. Exit application""")
        option = input()

        if option == "1":
            dept_name = get_department_name()
            db_dept.add_department(dept_name)

        elif option == "2":
            pass
        elif option == "3":
            pass
        elif option == "4":
            condition = False
        elif option == "5":
            print("Goodbye")
            sys.exit()
        else:
            print("Provided value is not correct!")







def get_department_name():
    while True:
        dept_name = input("Provide department name: ")
        if len(dept_name) >= 2:
            dept_name = dept_name[0].upper() + dept_name[1:]
            return dept_name
        else:
            print("Department name has to be at least 2 characters long")