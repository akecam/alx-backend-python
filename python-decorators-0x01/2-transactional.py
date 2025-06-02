import sqlite3
import functools

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


@with_db_connection
def get_user_by_id(conn, user_id):

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id, ))

    return cursor.fetchone()


def transactional(func):
    """
    transactional: gets when a particular databae gets an error
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = None
        for arg in args:
            if isinstance(arg, sqlite3.Connection):
                conn = arg
                break
        if conn is None:
            raise ValueError("No SQLite connection object found in arguments")

        try:
            result = func(*args, **kwargs)
            conn.commit()
            return result
        except Exception as e:
            conn.rollback()
            raise e
    return wrapper


@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))



update_user_email(user_id=1, new_email='Crawford_Cartwright@hotmail.com')
# user = get_user_by_id(user_id=1)
# print(user)