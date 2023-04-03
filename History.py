import mysql.connector
import datetime
from tkinter import *
from tkinter import messagebox


class History:
    def __init__(self):
        self.messages = []
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="azerty",
            database="myDiscord"
        )
        self.cursor = self.db.cursor()
        self.load_messages()

    def load_messages(self):
        query = "SELECT * FROM history"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for row in result:
            timestamp = row[0]
            nickname = row[1]
            content = row[2]
            message = f"[{timestamp}] {nickname}: {content}"
            self.messages.append(message)

    def add_message(self, nickname, content):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        message = f"[{timestamp}] {nickname}: {content}"
        self.messages.append(message)
        query = "INSERT INTO history (timestamp, nickname, content) VALUES (%s, %s, %s)"
        values = (timestamp, nickname, content)
        self.cursor.execute(query, values)
        self.db.commit()
