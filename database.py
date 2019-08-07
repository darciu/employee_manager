import sqlite3
from sqlite3 import Error
import datetime
import pandas as pd

class Database:
    def __init__(self):
        self.conn = self.create_connection("database.db")

    def create_connection(self, db_file):
        """Returns connection object with database"""
        try:
            conn = sqlite3.connect(db_file)
            return conn
        except Error as e:
            print(e)


class BuildDatabase(Database):
    """Create tables in database"""
    def __init__(self):
        super().__init__()
        self.conn.execute('PRAGMA foreign_keys = ON')
        sql_create_employees = """CREATE TABLE IF NOT EXISTS employees(
                                        employee_id integer PRIMARY KEY,
                                        firstName text NOT NULL,
                                        lastName text NOT NULL,
                                        sex integer NOT NULL,
                                        birth_year integer NOT NULL,
                                        basic_salary real NOT NULL,
                                        level text NOT NULL,
                                        department_id integer,
                                        position text NOT NULL,
                                        FOREIGN KEY (department_id) REFERENCES department(department_id));"""

        sql_create_department = """ CREATE TABLE IF NOT EXISTS departments(
                                        department_id integer PRIMARY KEY,
                                        department_name text NOT NULL);"""

        self.create_table(self.conn, sql_create_employees)
        self.create_table(self.conn, sql_create_department)



    def create_table(self,conn,sql_statement):
        """"""
        try:
            cur = conn.cursor()
            cur.execute(sql_statement)
            conn.commit()

        except Error as e:
            print(e)

class DepartmentDatabase(Database):

    def __init__(self):
        super().__init__()

    def add_department(self, dept_name):

        sql = "INSERT INTO departments(department_name) VALUES(?);"
        dataset = (dept_name,)
        cur = self.conn.cursor()

        cur.execute(sql,dataset)
        self.conn.commit()

    def return_dept_name_list(self):

        sql = "SELECT department_name FROM departments;"
        cur = self.conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        dept_list = []
        print("Available departments: ")
        for row in rows:
            dept_list.append(row[0])
        print(", ".join(dept_list))
        print()
        return dept_list

    def update_dept_name(self, dept_name, dept_name_new):

        sql = "UPDATE departments SET department_name = ? WHERE department_name = ?"
        dataset = (dept_name_new,dept_name)
        cur = self.conn.cursor()

        cur.execute(sql, dataset)
        self.conn.commit()

    def delete_department(self, dept_name):

        department_id = self.get_department_id(dept_name)

        sql1 = "DELETE FROM departments WHERE department_name = ?"
        sql2 = "UPDATE employees SET department_id = NULL WHERE department_id = ?"

        dataset1 = (dept_name,)
        dataset2 = (department_id,)

        cur = self.conn.cursor()
        cur.execute(sql1, dataset1)
        cur.execute(sql2,dataset2)

        self.conn.commit()

    def get_department_id(self, dept_name):
        sql = "SELECT department_id FROM departments WHERE department_name = ?"
        dataset = (dept_name,)
        cur = self.conn.cursor()
        cur.execute(sql, dataset)
        row = cur.fetchone()
        return row[0]

    def get_department_name(self,department_id):
        sql = "SELECT department_name FROM departments WHERE department_id = ?"
        dataset = (department_id,)
        cur = self.conn.cursor()
        cur.execute(sql, dataset)
        row = cur.fetchone()
        return row[0]

    def print_department_employees(self, department_id):
        n = datetime.datetime.now()
        cur = self.conn.cursor()
        if department_id != None:
            sql = "SELECT * FROM employees WHERE department_id = ?"
            dataset = (department_id,)
            cur.execute(sql, dataset)
        else:
            cur.execute("SELECT * FROM employees WHERE department_id IS NULL")
        rows = cur.fetchall()
        for row in rows:
            print("First name: ",row[1])
            print("Last name: ", row[2])
            print("Employee ID: ",row[0])
            if row[3] == 1:
                print("Sex: Male")
            elif row[3] == 0:
                print("Sex: Female")
            print("Age: ",int(n.year) - row[4])
            print("Basic salary: ", row[5])
            print("Level: ",row[6])
            print("Position: ",row[8])
            a = input("Press Enter...\n")


    def print_position_employees(self, position):
        n = datetime.datetime.now()
        cur = self.conn.cursor()
        sql = "SELECT * FROM employees WHERE position = ?"
        dataset = (position,)
        cur.execute(sql,dataset)

        rows = cur.fetchall()

        if len(rows) == 0:
            print("There are no employees no this position\n")
            a = input("Press Enter...")
            return

        for row in rows:
            print("First name: ", row[1])
            print("Last name: ", row[2])
            print("Employee ID: ", row[0])
            if row[3] == 1:
                print("Sex: Male")
            elif row[3] == 0:
                print("Sex: Female")
            print("Age: ", int(n.year) - row[4])
            print("Basic salary: ", row[5])
            print("Level: ", row[6])
            if row[7] == None:
                print("Department: ", row[7])
            else:
                department_name = self.get_department_name(row[7])
                print("Department: ", department_name)
            a = input("Press Enter to continue...\n")

    def check_ID(self, ID):

        sql = "SELECT * FROM employees WHERE employee_id = ?"
        dataset = (ID,)
        cur = self.conn.cursor()
        cur.execute(sql, dataset)
        row = cur.fetchone()
        return row

class EmployeeDatabase(Database):
    def __init__(self):
        super().__init__()



    def add_to_database(self, firstName, lastName, sex, birth_year, basic_salary, level, department_id, position):

        sql = "INSERT INTO employees(firstName,lastName,sex,birth_year,basic_salary, level, department_id, position) VALUES(?,?,?,?,?,?,?,?);"
        dataset = (firstName, lastName, sex, birth_year, basic_salary, level, department_id, position)
        cur = self.conn.cursor()
        cur.execute(sql,dataset)
        self.conn.commit()

    def update_name(self, firstName, employee_id):
        sql = "UPDATE  employees SET firstName = ? WHERE employee_id = ?"
        dataset = (firstName, employee_id)
        cur = self.conn.cursor()
        cur.execute(sql, dataset)
        self.conn.commit()
        print("First name has been successfully updated\n\nPress Enter to continue...")
        a = input()

    def update_surname(self, lastName, employee_id):
        sql = "UPDATE  employees SET lastName = ? WHERE employee_id = ?"
        dataset = (lastName, employee_id)
        cur = self.conn.cursor()
        cur.execute(sql, dataset)
        self.conn.commit()
        print("Last name has been successfully updated\n\nPress Enter to continue...")
        a = input()

    def update_basic_salary(self, basic_salary, employee_id):
        sql = "UPDATE  employees SET basic_salary = ? WHERE employee_id = ?"
        dataset = (basic_salary, employee_id)
        cur = self.conn.cursor()
        cur.execute(sql, dataset)
        self.conn.commit()
        print("Basic salary has been successfully updated\n\nPress Enter to continue...")
        a = input()

    def update_position(self, position, employee_id):
        sql = "UPDATE  employees SET position = ? WHERE employee_id = ?"
        dataset = (lastName, employee_id)
        cur = self.conn.cursor()
        cur.execute(sql, dataset)
        self.conn.commit()
        print("Position has been successfully updated\n\nPress Enter to continue...")
        a = input()

    def update_department_id(self, department_id, employee_id):
        sql = "UPDATE  employees SET department_id = ? WHERE employee_id = ?"
        dataset = (department_id, employee_id)
        cur = self.conn.cursor()
        cur.execute(sql, dataset)
        self.conn.commit()
        print("Department has been successfully updated\n\nPress Enter to continue...")
        a = input()

    def remove_employee_duplicates(self):
        """Removes duplicate employees from database by firstName, lastName, sex, birth_year set of columns"""
        sql = "DELETE FROM employees WHERE rowid NOT IN (SELECT MIN(rowid) FROM employees GROUP BY firstName, lastName, sex, birth_year);"
        cur = self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()

    def export_to_df(self):
        """Read employees table and return dataframe"""

        sql = "SELECT * FROM employees"
        df = pd.read_sql_query(sql, self.conn)

        return df

    def remove_employee(self,employee_id):
        sql = "DELETE FROM employees WHERE employee_id = ?"
        dataset = (employee_id,)
        cur = self.conn.cursor()
        cur.execute(sql,dataset)
        self.conn.commit()

        print("Employee has been successfull removed!\n")

    def get_min_salary(self):
        sql = "SELECT MIN(basic_salary) FROM employees"
        cur = self.conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        return row[0]

    def get_max_salary(self):
        sql = "SELECT MAX(basic_salary) FROM employees"
        cur = self.conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        return row[0]

    def get_average_salary(self):
        sql = "SELECT AVG(basic_salary) FROM employees"
        cur = self.conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        return row[0]

    def get_count_salary(self):
        sql = "SELECT COUNT(basic_salary) FROM employees"
        cur = self.conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        return row[0]

    def get_sum_salary(self):
        sql = "SELECT SUM(basic_salary) FROM employees"
        cur = self.conn.cursor()
        cur.execute(sql)
        row = cur.fetchone()
        return row[0]


    def get_count_lt_salary(self,basic_salary):
        sql = "SELECT COUNT(basic_salary) FROM employees WHERE basic_salary <= ?"
        dataset = (basic_salary,)
        cur = self.conn.cursor()
        cur.execute(sql,dataset)
        row = cur.fetchone()
        return row[0]
