import tkinter as tk
from tkinter import messagebox
import mysql.connector
import mysql.connector as mysql
import re


class Signup:
    def __init__(self, window):
        self.window = window
        self.window.title("Sign up")
        self.window.config(bg="#36393f")

        # Create label for each input field
        self.nickname_lbl = tk.Label(
            window, text="Nickname", bg="#36393f", fg="white")
        self.name_lbl = tk.Label(window, text="Name", bg="#36393f", fg="white")
        self.surname_lbl = tk.Label(
            window, text="Surname", bg="#36393f", fg="white")
        self.email_lbl = tk.Label(
            window, text="Email", bg="#36393f", fg="white")
        self.password_lbl = tk.Label(
            window, text="Password", bg="#36393f", fg="white")

        # Create entry for each input field
        self.nickname_ent = tk.Entry(window)
        self.name_ent = tk.Entry(window)
        self.surname_ent = tk.Entry(window)
        self.email_ent = tk.Entry(window)
        self.password_ent = tk.Entry(window, show="*")

        # Create submit button
        self.submit_btn = tk.Button(
            window, text="Submit", command=self.create_account)

        # Place labels, entries, and button in the window
        self.nickname_lbl.grid(row=0, column=0)
        self.nickname_ent.grid(row=0, column=1)
        self.name_lbl.grid(row=1, column=0)
        self.name_ent.grid(row=1, column=1)
        self.surname_lbl.grid(row=2, column=0)
        self.surname_ent.grid(row=2, column=1)
        self.email_lbl.grid(row=3, column=0)
        self.email_ent.grid(row=3, column=1)
        self.password_lbl.grid(row=4, column=0)
        self.password_ent.grid(row=4, column=1)
        self.submit_btn.grid(row=5, column=1)

    def create_account(self):
        # Get user input
        nickname = self.nickname_ent.get()
        name = self.name_ent.get()
        surname = self.surname_ent.get()
        email = self.email_ent.get()
        password = self.password_ent.get()

        # Verify user input
        if not nickname or not name or not surname or not email or not password:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        if len(nickname) < 3:
            messagebox.showerror(
                "Error", "Nickname must be at least 3 characters.")
            return

        if len(password) < 8:
            messagebox.showerror(
                "Error", "Password must be at least 8 characters.")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Error", "Invalid email.")
            return

        # Save user to database
        conn = mysql.connector.connect(
            host="localhost", user="root", password="azerty", database="myDiscord")
        cursor = conn.cursor()
        query = "INSERT INTO users (nickname, name, surname, email, password) VALUES (%s, %s, %s, %s, %s)"
        values = (nickname, name, surname, email, password)
        cursor.execute(query, values)
        conn.commit()

        # Close connection
        cursor.close()
        conn.close()

        messagebox.showinfo("Success", "Account created successfully.")
