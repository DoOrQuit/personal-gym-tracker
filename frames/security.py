import tkinter.messagebox
from tkinter import *
from tkinter.messagebox import showerror
import pandas as pd
import os

# Fetching the users list for displaying in OptionMenu
users_df = pd.read_csv("settings/users_list.csv")
USERS_LIST = [user for user in users_df.name]


class Security:
    def __init__(self):
        # -------- Window arrangement ------------------- #
        self.master = Tk()
        self.master.title("Gym Activity Tracker")
        self.master.geometry("600x300")
        self.security_passed = False
        self.user_name = StringVar(self.master, "User Name")
        self.user_pass = StringVar(self.master)
        # -------- IMG/(Banner) placing ----------------- #
        self.canvas = Canvas(self.master, width=600, height=156)
        self.image = PhotoImage(master=self.master, file="images/divide.png")
        self.canvas.create_image(300, 78, image=self.image)
        self.canvas.config(highlightthickness=0)
        self.canvas.grid(column=0, row=0, columnspan=4)
        # --------- Login labels ------------------------ #
        self.user_label = Label(self.master, text="User: ")
        self.user_label.grid(column=0, row=1, pady=(20, 5))
        self.password_label = Label(self.master, text="Password: ", padx=50)
        self.password_label.grid(column=0, row=2, pady=(0, 10))
        self.info_label = Label(self.master, text="(Optional)", anchor="e")
        self.info_label.grid(column=2, row=2, pady=(0, 10))
        # --------- Login Buttons ----------------------- #
        self.add_user = Button(self.master, text="➕ Add User", command=self.add_user)
        self.add_user.grid(column=2, row=1, pady=(20, 5))
        self.login_button = Button(self.master, text="Login", width=25, command=self.security_check)
        self.login_button.grid(column=1, row=3)
        # --------- Login Entries ----------------------- #
        self.user_drop_list = OptionMenu(self.master, self.user_name, *USERS_LIST)
        self.user_drop_list.config(width=24)
        self.user_drop_list.grid(column=1, row=1, pady=(20, 5))
        self.password_entry = Entry(self.master, width=30, textvariable=self.user_pass)
        self.password_entry.grid(column=1, row=2, pady=(0, 10))


    def run(self):
        self.master.mainloop()
        return self.security_passed


    @staticmethod
    def add_user():
        """Function creates a new profile and saves it in settings for further initialization"""
        new_user_window = Toplevel()
        new_user_window.focus()
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
        new_name_entry.focus()
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

            new_user_data = {"name": [f"{name}"], "password": [f"{password}"]}

            if password == confirm_password and name != "":

                # Checking if setting file exists. In this case data will be appended to existing file
                if os.path.isfile("settings/users_list.csv"):
                    existed_data = pd.read_csv("settings/users_list.csv")
                    new_id = int(len(existed_data.id))
                    data = pd.DataFrame(new_user_data, index=[new_id])
                    data.to_csv("settings/users_list.csv", mode="a", header=False)
                    new_user_window.destroy()
                else:
                    data = pd.DataFrame(new_user_data)
                    data.to_csv("settings/users_list.csv", mode="w", index_label="id", index=True)
                    new_user_window.destroy()
            else:
                if password != confirm_password:
                    showerror(title="Password Error", message='Passwords are not matching')
                if name == "":
                    showerror(title="Name Error", message='Please, enter a Name')

        new_user_button = Button(new_user_window, text="✔ Save", width=10, command=save_user)
        new_user_button.grid(column=1, row=3, pady=(20, 20))


    def security_check(self):
        """Method validates the user's name and password (if applied) entered
        and returns True if security check has been passed"""

        user_name_entered = self.user_name.get()
        user_password_entered = self.user_pass.get()

        data = pd.read_csv("settings/users_list.csv")
        database_user_pass = data.loc[data.name == f"{user_name_entered}", "password"]

        if (f"{user_name_entered}" in data["name"].values) and (str(*database_user_pass) == user_password_entered):
            self.security_passed = True
            self.master.destroy()
            print("It's SUCCESSES")
            return True

        elif f"{user_name_entered}" not in data["name"].values or str(*database_user_pass) != user_password_entered:
            tkinter.messagebox.showinfo(
                title="Login error",
                message="User does not exist or password for current user is incorrect.\n"
                        "Please check a spelling or create a new user"
            )

        else:
            print("Something went wrong with Security Check")