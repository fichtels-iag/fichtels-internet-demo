import sqlite3
import time
from datetime import datetime


def create_table(con, cur):
    with con:
        cur.execute(
            '''CREATE TABLE IF NOT EXISTS
            messages (
                timestamp int,
                messages text
            );''')

def get_all_messages():
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    create_table(con, cur)

    with con:
        cur.execute(
            '''SELECT * FROM messages;''')

    results = []
    for row in cur:
        results.append((datetime.utcfromtimestamp(row[0]).strftime('%Y-%m-%d %H:%M'), row[1]))

    con.close()
    return results


def add_data(message: str):
    if len(message) > 255:
        message = message[0:255]
        message += '...'
    con = sqlite3.connect('data.db')
    cur = con.cursor()
    create_table(con, cur)

    with con:
        cur.execute(
            '''INSERT INTO messages VALUES (?, ?)''',
            ([time.time(), message]))
    con.close()
