#!/usr/bin/python3

"""
Custom class based context manager for
Database connection
"""

import sqlite3


class DatabaseConnection:
    """
    DatabseConnecttion: connects to a database
    """

    def __init__(self, database: str):
        self.db: str = database

    def __enter__(self):
        conn = sqlite3.connect(self.db)
        self.cursor = conn.cursor()
        return self.cursor

    def __exit__(self, type, value, traceback):
        if self.cursor:
            self.cursor.close()


with DatabaseConnection("users.db") as cursor:
    # cursor.execute("CREATE TABLE users (id PRIMARY KEY, name VARCHAR, email VARCHAR)")
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()

    print(result)
