import os.path
import sqlite3 as sl
from datetime import datetime


def create_database():
    con = sl.connect('database/pole.db')
    with con:
        con.execute("""
            CREATE TABLE POLE (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                user_id TINYTEXT,
                pole_type TINYTEXT,
                rank INT,
                date DATE
            );
        """)


def get_pole_data(text):
    return 1, 2


def insert_pole(message):
    con = sl.connect('database/pole.db')
    text = message.text
    user_id = message.from_user.id
    pole_type, pole_rank = get_pole_data(text)
    date = datetime.now()
    sql = 'INSERT INTO USER (id, user_id, pole_type, rank, date) values(?, ?, ?, ?, ?)'
    data = [('NULL', user_id, pole_type, pole_rank, date)]


def validate_message(message):
    pass


def return_message(message):
    if os.path.exists('database/pole.db'):
        if validate_message(message):
            return insert_pole(message)
    else:
        create_database()
