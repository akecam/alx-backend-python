#!./.venv/bin/python3

"""
Python Generators that stream rows from an SQL database
"""

import mysql.connector

def stream_users():
    """
    Generator function to yield or report back row
    """
    fields = ["user_id", "name", "email", "age"]
    mydb = mysql.connector.connect(
        host="localhost",
        password="newone11",
        user="maceka"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `ALX_prodev`.`user_data`;")

    row = mycursor.fetchone()

    while row:
        dict_row = dict(zip(fields, row))
        yield dict_row
        row = mycursor.fetchone()

    
    
