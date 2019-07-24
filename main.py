from search_employee import search_menu
from manage_employee import manage_menu
import sys
from database import BuildDatabase

if __name__ == "__main__":
    db = BuildDatabase()
    db.conn.close()

    print("Welcome to the Text Employee Manager\n")

    condition = True
    while condition:
        print(""""Please choose what action do you want to perform:
                1. Search for an employee
                2. Manage employees
                3. Exit application""")
        option = input()
        if option == "1":
            search_menu()
        elif option == "2":
            manage_menu()
        elif option == "3":
            print("Goodbye")
            sys.exit()
        else:
            print("Please provide a correct option!")