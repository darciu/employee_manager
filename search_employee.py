import sys
def regexp_search():
    pass


def vertical_strutcture():
    pass




def search_menu():
    condition = True
    while condition:
        print("""Please select one of the following options:
                1. Search by first and last name.
                2. See vertical structure of the organization
                3. Back
                4. Exit application""")
        option = input()
        if option == "1":
            regexp_search()
        elif option == "2":
            vertical_strutcture()
        elif option == "3":
            condition = False
        elif option == "4":
            print("Goodbye")
            sys.exit()
        else:
            print("Provided answer is not correct!")


