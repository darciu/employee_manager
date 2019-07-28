import sqlite3
from sqlite3 import Error
import datetime

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
                                        position integer NOT NULL,
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
        dataset = (dept_name,dept_name_new)
        cur = self.conn.cursor()

        cur.execute(sql, dataset)
        self.conn.commit()

    def delete_department(self, dept_name):

        sql = "DELETE FROM departments WHERE department_name = ?"
        dataset = (dept_name,)
        cur = self.conn.cursor()
        cur.execute(sql, dataset)
        self.conn.commit()

    def get_department_id(self, dept_name):
        sql = "SELECT department_id FROM departments WHERE department_name = ?"
        dataset = (dept_name,)
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
            if row[3] == 1:
                print("Sex: Male")
            elif row[3] == 0:
                print("Sex: Female")
            print("Age: ",int(n.year) - row[4])
            print("Basic salary: ", row[5])
            print("Level: ",row[6])
            print("Position: ",row[8])
            a = input("Press Enter...\n")





class EmployeeDatabase(Database):
    def __init__(self):
        super().__init__()

    def add_to_database(self, firstName, lastName, sex, birth_year, basic_salary, level, department_id, position):

        sql = "INSERT INTO employees(firstName,lastName,sex,birth_year,basic_salary, level, department_id, position) VALUES(?,?,?,?,?,?,?,?);"
        dataset = (firstName, lastName, sex, birth_year, basic_salary, level, department_id, position)
        cur = self.conn.cursor()
        cur.execute(sql,dataset)
        self.conn.commit()
