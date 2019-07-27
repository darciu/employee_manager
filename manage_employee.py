import sys
from employees import Trainee, Junior, Mid, Senior, Administrative, Executive




def manage_menu():
    print("This module allows to add, modify or remove any employee from the database")
    condition = True
    while condition:
        print("""Please select one of the following options:
                1. Manage single employee (add or search)
                2. Load employees from Excel file
                3. Back
                4. Exit application""")
        option = input()
        if option == "1":
            manage_single_menu()
        elif option == "2":
            pass
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
                2. Search employee
                3. Back
                4. Exit application""")
        option = input()
        if option == "1":
            add_single_employee()
        elif option == "2":
            pass
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
            personal_data = get_personal_data()
            Trainee(personal_data[0],personal_data[1],personal_data[2],personal_data[3],
                    personal_data[4]).add_to_database()


        elif option.lower() == "junior":
            pass
        elif option.lower() == "mid":
            pass
        elif option.lower() == "senior":
            pass
        elif option.lower() == "administrative":
            pass
        elif option.lower() == "manager":
            pass
        elif option.lower() == "executive":
            pass
        elif option == "":
            condition = False
        else:
            print("Invalid position name")



def get_personal_data():

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


def get_department():
    while True:
        department = input("Please provide department: ")


# uzupełnić dodawanie innych typów pracowników
# dodać wybór department (na podstawie dostępnych w bazie) oraz dodawanie department z managera
