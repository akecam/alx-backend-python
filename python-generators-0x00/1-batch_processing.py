#!/usr/bin/python3

"""
Batch Processing Large Data
"""

import mysql.connector


def stream_users_in_batches(batch_size: int):
    """
    stream_users_in_batches: streams the batches of users in the database

    Args:
        batch_size: int -> number of streams to yield at once
    """
    fields = ["user_id", "name", "email", "age"]

    mydb = mysql.connector.connect(
        host="localhost", user="maceka", password="newone11", database="ALX_prodev"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM user_data;")

    for data in mycursor.fetchmany(size=batch_size):
        new_data = dict(zip(fields, data))
        yield new_data


def batch_processing(batch_size: int):
    """
    batch_processing: streams the batches of users in the database
                        and analyzes to produce a certain output

    Args:
        batch_size: int -> number of streams to yield at once
    """

    for users in stream_users_in_batches(batch_size):
        if users["age"] >= 25:
            for key, value in users.items():
                if key == "age":
                    users[key] = float(users[key])

            print(users)


def main():

    batch_processing(5)


if __name__ == "__main__":
    main()
