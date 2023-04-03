import tkinter as tk
import datetime
import mysql.connector


class Chatroom:
    def __init__(self, nickname):
        self.nickname = nickname
        self.messages = []
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="azerty",
            database="myDiscord"
        )
        self.cursor = self.db.cursor()

        self.root = tk.Tk()
        self.root.title('MyDiscord')
        self.root.geometry('600x600')
        self.root.configure(bg='#36393f')

        self.message_frame = tk.Frame(self.root, bg='#36393f')
        self.message_frame.pack(fill=tk.BOTH, expand=True)

        self.chat_log = tk.Text(self.message_frame, bg='#2f3136', fg='#ffffff')
        self.chat_log.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.message_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.chat_log.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.chat_log.yview)

        self.message_entry = tk.Entry(self.root, bg='#2f3136', fg='#ffffff')
        self.message_entry.pack(fill=tk.X, padx=10, pady=10)

        self.send_button = tk.Button(
            self.root, text='Send', command=self.send_message, bg='#7289da', fg='#ffffff')
        self.send_button.pack(padx=10, pady=10)

        self.root.bind('<Return>', self.send_message)
        self.root.bind('<Escape>', self.quit)

        self.load_messages()

        self.root.mainloop()

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
            self.chat_log.insert(tk.END, message + '\n')

    def send_message(self, event=None):
        content = self.message_entry.get().strip()
        if content:
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            message = f"[{timestamp}] {self.nickname}: {content}"
            self.messages.append(message)
            self.chat_log.insert(tk.END, message + '\n')
            self.chat_log.see(tk.END)
            self.message_entry.delete(0, tk.END)

            query = "INSERT INTO history (timestamp, nickname, content) VALUES (%s, %s, %s)"
            values = (timestamp, self.nickname, content)
            self.cursor.execute(query, values)
            self.db.commit()

    def quit(self, event=None):
        self.db.close()
        self.root.destroy()


my_Chatroom = Chatroom('Sylvie')
