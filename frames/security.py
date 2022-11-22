from tkinter import *
from tkinter.messagebox import showerror
import pandas as pd
import os


class Security:
    def __init__(self):
        # -------- Window arrangement ---------- #
        self.root = Tk()
        self.root.title("Gym Activity Tracker")
        # self.root.config(pady=5, padx=5)
        self.root.minsize(600, 300)
        # -------- IMG/(Banner) placing ----------------- #
        self.canvas = Canvas(width=600, height=156)
        self.image = PhotoImage(file="images/divide.png")
        side_banner = self.canvas.create_image(300, 78, image=self.image)
        self.canvas.config(highlightthickness=0)
        self.canvas.grid(column=0, row=0, columnspan=4)
        self.login()

        self.root.mainloop()

    def login(self):
        # --------- Login labels ---------- #
        user_label = Label(text="User: ")
        user_label.grid(column=0, row=1, pady=(20, 5))
        password_label = Label(text="Password: ", padx=50)
        password_label.grid(column=0, row=2, pady=(0, 10))
        info_label = Label(text="(Optional)", anchor="e")
        info_label.grid(column=2, row=2)
        # --------- Login Buttons ---------- #
        add_user = Button(text="➕ Add User", command=self.add_user)
        add_user.grid(column=2, row=1, pady=(20, 0))
        login_button = Button(text="Login", width=17, command=self.security_check)
        login_button.grid(column=0, row=3)
        # --------- Login Entries ---------- #
        user_name = StringVar(self.root)
        user_name.set("antony")
        user_drop_list = OptionMenu(self.root, user_name, "antony")
        user_drop_list.grid(column=1, row=1, pady=(20, 5))
        password_entry = Entry(width=30)
        password_entry.grid(column=1, row=2)

    @staticmethod
    def add_user():
        """Function creates a new profile and saves it in settings for further initializing of a user"""
        new_user_window = Tk()
        new_user_window.title("New User")
        new_user_window.minsize(300, 150)
        new_user_window.attributes("-topmost", True)
        # ----------------- Labels -------------------- #
        new_user_name = Label(new_user_window, text="User Name:")
        new_user_name.grid(column=0, row=0, pady=(20, 5), padx=30)
        new_user_pass = Label(new_user_window, text="Password:")
        new_user_pass.grid(column=0, row=1, pady=(5, 5), padx=30)
        new_pass_check = Label(new_user_window, text="Repeat Password:")
        new_pass_check.grid(column=0, row=2, padx=30)
        # ----------------- Entries -------------------- #
        new_name_entry = Entry(new_user_window)
        new_name_entry.grid(column=1, row=0, pady=(20, 5))
        new_pass_entry = Entry(new_user_window)
        new_pass_entry.grid(column=1, row=1, pady=(5, 5))
        confirm_pass_entry = Entry(new_user_window)
        confirm_pass_entry.grid(column=1, row=2)
        # ----------------- Buttons -------------------- #

        def save_user():
            """Fetches and saves a data taken from widgets to save to a local settings file"""
            name = new_name_entry.get()
            password = new_pass_entry.get()
            confirm_password = confirm_pass_entry.get()

            if password == confirm_password:
                # Creating a DICT from TK Entries as data set to use with a pandas lib
                new_user = {f"{name}": f"{password}"}
                data = pd.DataFrame(new_user, index=[0])
                # Checking if setting file exists. In this case data will be appended to existing file
                if os.path.isfile("../settings/users_list.csv"):
                    print("Found!")
                    # data.to_csv("../settings/users_list.csv", mode="a")
                else:
                    print("not found")
                    # data.to_csv("../settings/users_list.csv", mode="w")
            else:
                showerror(title="Password Error", message='Passwords are not matching')

        new_user_button = Button(new_user_window, text="✔ Save", width=10, command=save_user)
        new_user_button.grid(column=1, row=3, pady=(20, 20))

    def security_check(self) -> bool:
        pass

    def users_list(self):
        pass
