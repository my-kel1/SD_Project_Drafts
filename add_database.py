import sqlite3
import random


class addData:

    list_info = []

    def __init__(self):

        self.conn = sqlite3.connect('information.db')
        self.cursor = self.conn.cursor()

    def create_table_info(self):

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS info(
                            medicine_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            Medicine TEXT,
                            Days Intake TEXT,
                            Time Intake TEXT)''')

        self.conn.commit()

    def insert_data_info(self, data):

        data_list = data

        self.cursor.executemany('INSERT INTO info VALUES (?,?,?)', data_list)

        self.conn.commit()


db = addData()
data = [('bio', '3', '12:00pm')]
db.create_table_info()
db.insert_data_info(data)

