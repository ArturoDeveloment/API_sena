from typing import Dict, Any
import mysql.connector as conn
from dotenv import load_dotenv
import os

load_dotenv()

class Queries:

    connection = conn.connect(
        host=os.getenv("host"),
        user=os.getenv("user"),
        password=os.getenv("password"),
        database=os.getenv("db"),
        port = os.getenv("port")
    )

    cursor = connection.cursor()

    def execute_query(self, query):
        self.cursor.execute(query)
        result_set = self.cursor.fetchall()
        return result_set

    def insert(self, table: str, columns_values: Dict[str, Any]):
        columns = ",".join(list(columns_values.keys()))
        values = ",".join(map(lambda dato: f"'{dato}'", columns_values.values()))
        query = f"INSERT INTO {table} ({columns}) VALUES ({values});"
        self.execute_query(query)
        self.connection.commit()

    def delete(self, table: str, columns_values: Dict[str, Any]):
        column_value = "=".join([f"{column} = '{value}'" for column, value in columns_values.items()])
        query = f"DELETE FROM {table} WHERE {column_value};"
        self.execute_query(query)
        self.connection.commit()

    def update(self, table: str, columns_where: Dict[str, Any], columns_values: Dict[str, Any]):
        column_value = ", ".join([f"{column}='{value}'" for column, value in columns_values.items()])
        where = [f"{column} = '{value}'" for column, value in columns_where.items()]
        where = " AND ".join(where) if len(columns_where) > 1 else "".join(where)
        query = f"UPDATE {table} SET {column_value} WHERE {where};"
        self.execute_query(query)
        self.connection.commit()

    def select(self, table: str, columns_where: Dict[str, Any] = None, columns: list = ["*"]):
        columns = "".join(columns) if columns[0] == "*" else ", ".join(columns)
        where = ""
        if columns_where is not None:
            where = [f"{column} = '{value}'" for column, value in columns_where.items()]
            where = " AND ".join(where) if len(columns_where) > 1 else "".join(where)
            where = f"WHERE {where}"
        query = f"SELECT {columns} FROM {table} {where};"
        result_set = self.execute_query(query)
        return result_set

    def close(self):
        self.cursor.close()
        self.connection.close()

connection: conn.MySQLConnection | Queries = Queries()

def get_conn():
    return connection