import pandas as pd
import os
import sys

from employees import Trainee, Junior, Mid, Senior, Manager, Administrative, Executive

def get_excel_file():
    """Returns pandas dataframe"""
    for file in os.listdir('input'):
        if file.endswith('.xlsx') or file.endswith('.xls'):
            df = pd.read_excel("input\\" + file)
            return df

def import_df_conditions(df):

    columns_list = ['firstName','lastName','sex','birth_year','basic_salary','position']

    if df is None:
        print("Could not find Excel file in input directory!\n")
        return False

    if not pd.Series(columns_list).isin(df.columns).all():
        print("Could not find all necessary columns in dataframe")
        return False

    return True

def import_employees():

    df = get_excel_file()
    if not import_df_conditions(df):
        return

    # dataframe has passed input conditions

    question = input("There are {0} records in imported dataframe. Do you wish to add them to the database? If so, write Y ".format(df.shape[0]))

    if question.upper() != "Y":
        return

    for index, row in df.iterrows():
        class_arguments = list([row['firstName'], row['lastName'], row['sex'], row['birth_year'], row['basic_salary'], None])
        emp_class_dictionary = {"Trainee": Trainee(*class_arguments),
                                "Junior": Junior(*class_arguments),
                                "Mid": Mid(*class_arguments),
                                "Senior": Senior(*class_arguments),
                                "Administrative": Administrative(*class_arguments),
                                "Manager": Manager(*class_arguments),
                                "Executive": Executive(*class_arguments)}


        emp = emp_class_dictionary.get(row['position'])
        emp.add_to_database()




def import_export_employees():
    condition = True
    while condition:
        print("""Please select one of the following options:
                1. Import employees from input folder
                2. Export employees to output folder
                3. Back
                4. Exit application""")
        option = input()
        if option == "1":
            import_employees()
        elif option == "2":
            pass
        elif option == "3":
            condition = False
        elif option == "4":
            sys.exit()