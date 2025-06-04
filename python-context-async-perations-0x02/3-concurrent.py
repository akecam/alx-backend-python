#!/usr/bin/python3

"""
Objective: Run multiple database queries concurrently using asyncio.gather.

Instructions:

    Use the aiosqlite library to interact with SQLite asynchronously. To learn more about it, click here.

    Write two asynchronous functions: async_fetch_users() and async_fetch_older_users() that fetches all users and users older than 40 respectively.

    Use the asyncio.gather() to execute both queries concurrently.

    Use asyncio.run(fetch_concurrently()) to run the concurrent fetch

"""

import aiosqlite
import asyncio



async def async_fetch_users():
    """
    async_fetch_users: fetch all users
    """

    async with aiosqlite.connect("user.db") as db:
        
        async with db.execute("SELECT * FROM users") as data:

            return await data.fetchall()


async def async_fetch_older_users():
    """
    async_fetch_older_users: fetch older users above 40
    """

    async with aiosqlite.connect("user.db") as db:
        
        async with db.execute("SELECT * FROM users WHERE age > :age", {"age": 40}) as data:

            return await data.fetchall()


async def fetch_concurrently():
    """
    fetch_concurrently: fetch all users asynchronously with the two function
    """

    users, older_users = await asyncio.gather(async_fetch_older_users(), async_fetch_users())

    print("All Users:")
    print(users)
    print("\nUsers older than 40:")
    print(older_users)



if __name__ == "__main__":

    asyncio.run(fetch_concurrently())