"""
A python database setup for `user`
"""

import csv
import mysql.connector
from uuid import uuid4


def connect_db():
    """
    Conects to the database of application
    """
    try:
        mydb = mysql.connector.connect(
            host="localhost", user="maceka", password="newone11"
        )
        return mydb
    except mysql.connector.Error as err:
        return False


def create_database(connection: mysql.connector.MySQLConnection):
    """
    Creates the database

    Args:
        connection: Object with MySql connection
    """

    mycursor = connection.cursor()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS `ALX_prodev`;")


def connect_to_prodev():
    """
    Connects to the database ALX_prodev
    """
    try:
        mydb = mysql.connector.connect(
            host="localhost", user="maceka", password="newone11", database="ALX_prodev"
        )
        return mydb
    except mysql.connector.Error as err:
        return False


def create_table(connection: mysql.connector.MySQLConnection):
    """
    Creates the user_data table if not exist

    Args:
        connection: mysql object
    """

    mycursor = connection.cursor()
    mycursor.execute(
        "CREATE TABLE IF NOT EXISTS `ALX_prodev`.`user_data`(user_id CHAR(36) PRIMARY KEY, name VARCHAR(255) NOT NULL, email VARCHAR(90) NOT NULL, age DECIMAL NOT NULL);"
    )


def insert_data(connection: mysql.connector.MySQLConnection, data: str):
    """
    Insert data into table in database

    Args:
        connection: mysql Object
        data: data tuple to insert
    """

    mycursor = connection.cursor()

    sql = "INSERT INTO `ALX_prodev`.`user_data` (user_id, name, email, age) VALUES (%s, %s, %s, %s)"
    read_csv = csv_file(data)

    for row in read_csv:
        print(row)
        mycursor.execute(sql, row)

    connection.commit()

def csv_file(path: str):
    """
    Reads a csv file and parses it as generator
    """
    with open(path, newline='') as file:
        reader = csv.reader(file)
        # sys.getsizeof(reader)
        next(reader) # header cut off

        for line in reader:
            line[2] = float(line[2]) # type: ignore
            line.insert(0, str(uuid4()))
            yield tuple(line)