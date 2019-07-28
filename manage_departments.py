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
            print("{0} department has been added to database!\n".format(dept_name))

        elif option == "2":
            dept_list = db_dept.return_dept_name_list()
            print("Write down the name of department you want to change")
            dept_name = get_department_name()

            if dept_name in dept_list:
                print("Please provide new name")
                dept_name_new = get_department_name()
                db_dept.update_dept_name(dept_name,dept_name_new)
                print("{0} department has changed name to {1}.\n".format(dept_name,dept_name_new))
            else:
                print("There is no {0} department in database!\n".format(dept_name))



        elif option == "3":
            dept_list = db_dept.return_dept_name_list()
            print("Write down the name of department you want to remove")
            dept_name = get_department_name()
            if dept_name in dept_list:
                question = input("In order to remove this department from database, please write Y")
                if question.upper() == "Y":
                    db_dept.delete_department(dept_name)
                    print("{0} department has been successfully removed from database!\n".format(dept_name))
            else:
                print("There is no {0} department in database!\n".format(dept_name))

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