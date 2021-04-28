# models.py — handles everything that involves a Database.
import datetime
import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('resources/employees.db')
        self.create_employees_table()

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def create_employees_table(self):

        query = """
        CREATE TABLE IF NOT EXISTS "Employees" (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          FirstName TEXT,
          SecondName TEXT,
          Experience TEXT,
          Salary INTEGER,
          HiredOn Date DEFAULT CURRENT_DATE,
          FiredOn Date
        );
        """

        self.conn.execute(query)



class EmployeesModel:
    TABLENAME = "Employees"

    def __init__(self):
        self.conn = sqlite3.connect('resources/employees.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def get_by_id(self, _id):
        where_clause = f" WHERE id={_id}"
        return self.list_items(where_clause)

    def create(self, params):
        print (params)
        query = f'insert into {self.TABLENAME} ' \
                f'(FirstName, SecondName, Experience, Salary) ' \
                f'values ("{params.get("FirstName")}","{params.get("SecondName")}",' \
                f'"{params.get("Experience")}","{params.get("Salary")}")'
        result = self.conn.execute(query)
        return self.get_by_id(result.lastrowid)

    def delete(self, id):
        query = f'UPDATE {self.TABLENAME} ' \
                f'SET FiredOn =  DATE() ' \
                f'WHERE id = {id}'
        print (query)
        self.conn.execute(query)
        return self.list_items()

    def update(self, item_id, update_dict):
        """
        column: value
        Title: new title
        """
        set_query = ", ".join([f'{column} = {value}'
                     for column, value in update_dict.items()])

        query = f"UPDATE {self.TABLENAME} " \
                f"SET {set_query} " \
                f"WHERE id = {item_id}"
        self.conn.execute(query)
        return self.get_by_id(item_id)

    def list_items(self, where_clause=""):
        query = f"SELECT id, FirstName, SecondName, Experience, Salary, HiredOn, FiredOn " \
                f"from {self.TABLENAME}" + where_clause
        print (query)
        result_set = self.conn.execute(query).fetchall()
        result = [{column: row[i]
                  for i, column in enumerate(result_set[0].keys())}
                  for row in result_set]
        return result
