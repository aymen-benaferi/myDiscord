import tkinter as tk
from SignUp import Signup
from SignIn import Signin


class FrontPage:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('MyDiscord')
        self.root.geometry('400x200')
        self.root.configure(bg='#36393f')

        self.label = tk.Label(self.root, text='Welcome to MyDiscord!',
                              fg='#ffffff', font=('Arial', 16), bg='#36393f')
        self.label.pack(pady=20)

        self.signup_button = tk.Button(
            self.root, text='Sign up', command=self.show_signup, bg='#7289da', fg='#ffffff')
        self.signup_button.pack(padx=20, pady=10, side=tk.LEFT)

        self.signin_button = tk.Button(
            self.root, text='Sign in', command=self.show_signin, bg='#7289da', fg='#ffffff')
        self.signin_button.pack(padx=20, pady=10, side=tk.RIGHT)

        self.root.mainloop()

    def show_signup(self):
        signup_window = tk.Toplevel(self.root)
        Signup(signup_window)

    def show_signin(self):
        signin_window = tk.Toplevel(self.root)
        Signin(signin_window)


my_frontpage = FrontPage()
