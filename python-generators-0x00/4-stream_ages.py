#!/usr/bin/python3

"""
Memory -Efficient Aggregation with Generators
"""

import mysql.connector
import statistics

def stream_users_ages():
    """
    stream_users_ages: connect to db and gets user ages

    Args:
        None
    """

    mydb = mysql.connector.connect(
        host="localhost",
        user="maceka",
        password="newone11",
        database="ALX_prodev"
    )

    mycursor = mydb.cursor(dictionary=True)

    mycursor.execute("SELECT * FROM user_data;")

    data = mycursor.fetchone()

    while data:
        yield data
        data = mycursor.fetchone()


def calculate_avg_age():

        
    avg_value = statistics.mean((d['age'] for d in stream_users_ages()))

    print(f"Avergae age of users: {avg_value}")


# def main():
    
#     calculate_avg_age()


# if __name__ := "__main__":
#     main()