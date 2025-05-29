#!/usr/bin/python3

"""
Implements a pagination function to fetch users
of next page when needed
"""

seed = __import__("seed")

def paginate_users(page_size, offset):
    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows


def lazy_pagination(page_size):
    """
    lazy_paginate: lazy load a group of users
    using generators
    """
    
    offset = 0

    while True:
        yield paginate_users(page_size, offset)
        offset = offset * page_size
