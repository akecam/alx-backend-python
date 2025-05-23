#!/usr/bin/python3

import mysql.connector

def connect_to_prodev() -> mysql.connector.MySQLConnection:
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

def get_data(connection: mysql.connector.MySQLConnection):
    """
    Get data into table in database

    Args:
        connection: mysql Object
    """

    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM `ALX_prodev`.`user_data` LIMIT 6;")

    result = mycursor.fetchall()

    print(result)

    for row in result:
        print(row)


if __name__ == "__main__":

    connection = connect_to_prodev()
    
    get_data(connection)