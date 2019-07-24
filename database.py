import sqlite3
from sqlite3 import Error

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
                                        level text NOT NULL);"""

        self.create_table(self.conn, sql_create_employees)

    def create_table(self,conn,sql_statement):
        """"""
        try:
            cur = conn.cursor()
            cur.execute(sql_statement)
        except Error as e:
            print(e)



class EmployeeDatabase(Database):
    def __init__(self):
        super().__init__()

    def add_to_database(self, firstName, lastName, sex, birth_year, basic_salary, level):

        sql = "INSERT INTO employees(firstName,lastName,sex,birth_year,basic_salary, level) VALUES(?,?,?,?,?,?)"
        dataset = (firstName, lastName, sex, birth_year, basic_salary, level)
        cur = self.conn.cursor()

        cur.execute(sql,dataset)
        self.conn.commit()
