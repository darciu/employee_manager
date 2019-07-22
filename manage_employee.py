import sys



def manage_menu():
    print("This module allows to add, modify or remove any employee from the database")
    condition = True
    while condition:
        print("""Please select one of the following options:
                1. Search by first and last name
                2. Back
                3. Exit application""")
        option = input()
        if option == "1":
            pass
        elif option == "2":
            condition = False
        elif option == "3":
            sys.exit()
        else:
            print("Provided answer is not correct!")



