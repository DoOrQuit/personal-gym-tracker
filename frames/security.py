from tkinter import *
import pandas as pd


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
        # --------- Login Buttons ---------- #
        users_list_button = Button(text="All Users >", command=self.users_list)
        users_list_button.grid(column=2, row=1, pady=(20, 0))
        login_button = Button(text="Login", width=17, command=self.security_check)
        login_button.grid(column=0, row=3)
        # --------- Login Entries ---------- #
        user_entry = Entry(width=30)
        user_entry.config()
        user_entry.grid(column=1, row=1, pady=(20, 5))
        password_entry = Entry(width=30)
        password_entry.grid(column=1, row=2)

    def logout(self):
        pass

    def security_check(self) -> bool:
        pass

    def users_list(self):
        pass
