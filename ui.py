from tkinter import *
from tkinter import ttk


class AppInterface:
    def __init__(self):
        # -------- Window arrangement ---------- #
        self.root = Tk()
        self.root.title("Gym Activity Tracker")
        # self.root.config(pady=5, padx=5)
        self.root.minsize(900, 600)
        # -------- IMG/(Banner) placing ----------------- #
        self.canvas = Canvas(width=300, height=700)
        self.image = PhotoImage(file="images/main_img_original.png")
        side_banner = self.canvas.create_image(150, 350, image=self.image)
        self.canvas.config(highlightthickness=0)
        self.canvas.grid(column=0, row=0, rowspan=30)

        self.login()

        self.root.mainloop()

    def window_structure(self):
        # -------- Tabs arrangement ------------ #
        self.tab_control = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab3 = ttk.Frame(self.tab_control)
        self.tab4 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text="Body Progress")
        self.tab_control.add(self.tab2, text="Program 1")
        self.tab_control.add(self.tab3, text="Program 2")
        self.tab_control.add(self.tab4, text="Program 3")
        self.tab_control.pack(expand=1, fill="both")
        self.label1 = Label(self.tab1, text="Lets dive into the world of computers")
        self.label1.grid(row=0, column=0)
        self.label2 = Label(self.tab2, text="I'm number 2")
        self.label2.grid(row=0, column=0)

    def login(self):
        # --------- Login labels ---------- #
        user_label = Label(text="User: ", padx=20)
        user_label.grid(column=1, row=14)
        password_label = Label(text="Password: ", padx=20)
        password_label.grid(column=1, row=15)
        # --------- Login Buttons ---------- #
        users_list_button = Button(text="All Users >", padx=10, command=self.users_list)
        users_list_button.grid(column=3, row=14)
        login_button = Button(text="Login", width=17, command=self.security_check)
        login_button.grid(column=2, row=16)
        # --------- Login Entries ---------- #
        user_entry = Entry()
        user_entry.config()
        user_entry.grid(column=2, row=14)
        password_entry = Entry()
        password_entry.grid(column=2, row=15)


    def logout(self):
        pass

    def security_check(self) -> bool:
        pass

    def users_list(self):
        pass


