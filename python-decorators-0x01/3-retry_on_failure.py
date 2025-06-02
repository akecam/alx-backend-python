import time
import sqlite3 
import functools

#### paste your with_db_decorator here

def with_db_connection(func):
    """
    with_db_connection: connects to a database
    and closes the connection after task has been done
    """
    @functools.wraps(func)

    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        result = func(conn, **kwargs)
        conn.close()

        return result

    return wrapper


def retry_on_failure(retries, delay):
    """
    Retries execution when there's a failure
    """

    def inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            last_exception = None
               
            for _ in range(0, retries):
                try:
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    last_exception = e
                    time.sleep(delay)
            
            if last_exception:
                raise last_exception
        return wrapper

    return inner


@with_db_connection
@retry_on_failure(retries=3, delay=2)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    
    return cursor.fetchall()


#### attempt to fetch users with automatic retry on failure
users = fetch_users_with_retry()
print(users)