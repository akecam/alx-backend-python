#!/usr/bin/python3

"""
Reusable Query Context Manager

    Create a reusable context manager that takes a
    query as input and executes it, managing both connection and the query execution
"""

import sqlite3


class ExecuteQuery:
    """
    ExecuteQuery: takes a query as input and executes it
    managing both connection and the query execution
    """

    def __init__(self, query: str, query_parameter: dict[str, int] = None) -> None:
        """
        Initializes the ExecuteQuery class.

        Args:
            query: the query to execute
            query_parameter: parameter for the query
        """
        self.query: str = query
        self.query_parameter: str = query_parameter

    def __enter__(self):
        mydb = sqlite3.connect("user.db")
        self.userdb_cursor = mydb.cursor()

        if self.query_parameter is None:
            self.userdb_cursor.execute(f"{self.query}")
        else:
            self.userdb_cursor.execute(f"{self.query}", self.query_parameter)

        all_users = self.userdb_cursor.fetchall()

        return all_users

    def __exit__(self, type, value, traceback):
        if self.userdb_cursor:
            self.userdb_cursor.close()


if __name__ := "__main__":

    with ExecuteQuery(
        "CREATE TABLE IF NOT EXISTS users (id PRIMARY KEY, name VARCHAR, email VARCHAR, age INT)"
    ) as conn:
        print(conn)

    with ExecuteQuery("SELECT * FROM users WHERE age > :age", {"age": 6}) as conn:
        print(conn)
