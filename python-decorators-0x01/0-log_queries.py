import sqlite3
import functools
from datetime import datetime

### decorator to log SQL queries

def log_queries(func):
    """
    Log queries: logs all queries sent to the function
    """
    @functools.wraps(func)

    def wrapper(*arg, **kwargs):
        print(f"{datetime.now()}: __{func.__name__}__.{kwargs['query']}")
        func(*arg, **kwargs)

        return None
    return wrapper


@log_queries
def fetch_all_users(query):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    users = fetch_all_users(query="CREATE TABLE users (id PRIMARY KEY, name VARCHAR, email VARCHAR)")
    users = fetch_all_users(query="SELECT * FROM users")