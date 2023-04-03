import mysql.connector
from tkinter import *
from tkinter import messagebox

import mysql.connector
from tkinter import *
from tkinter import messagebox


class Signin:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign In")
        self.root.geometry("200x200")
        self.root.configure(bg="#2C2F33")

        # Create label and entry for nickname
        self.label_nickname = Label(
            self.root, text="Nickname", fg="#FFFFFF", bg="#2C2F33")
        self.label_nickname.pack()
        self.entry_nickname = Entry(self.root)
        self.entry_nickname.pack()

        # Create label and entry for password
        self.label_password = Label(
            self.root, text="Password", fg="#FFFFFF", bg="#2C2F33")
        self.label_password.pack()
        self.entry_password = Entry(self.root, show="*")
        self.entry_password.pack()

        # Create sign in button
        self.button_signin = Button(
            self.root, text="Sign In", command=self.signin, bg="#7289DA", fg="#FFFFFF")
        self.button_signin.pack(pady=10)

    def signin(self):
        # Get nickname and password from entries
        nickname = self.entry_nickname.get()
        password = self.entry_password.get()

        # Connect to the MySQL database
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="azerty",
            database="myDiscord"
        )

        # Create a cursor object
        mycursor = mydb.cursor()

        # Execute SQL query to check if the user exists and the password is correct
        sql = "SELECT * FROM users WHERE nickname = %s AND password = %s"
        val = (nickname, password)
        mycursor.execute(sql, val)
        result = mycursor.fetchone()

        if result is not None:
            # User is authenticated, show success message
            messagebox.showinfo("Success", "You have been signed in!")
            self.root.destroy()  # Close the sign in window

        else:
            # User is not authenticated, show error message
            messagebox.showerror("Error", "Invalid nickname or password")
