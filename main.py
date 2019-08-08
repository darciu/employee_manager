from modules.search_employee import search_menu
from modules.manage_employee import manage_menu
from modules.manage_departments import manage_dept_menu
import sys
from modules.database import BuildDatabase

if __name__ == "__main__":
    """Welcome Menu"""
    db = BuildDatabase()
    db.conn.close()

    print("Welcome to the Text Employee Manager\n")

    condition = True
    while condition:
        print(""""Please choose what action do you want to perform:
                1. Search for an employee
                2. Manage employees
                3. Manage departments
                4. Exit application""")

        option = input()
        if option == "1":
            search_menu()
        elif option == "2":
            manage_menu()
        elif option == "3":
            manage_dept_menu()
        elif option == "4":
            print("Goodbye")
            sys.exit()
        else:
            print("Invalid value!")