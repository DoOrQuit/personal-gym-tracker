from tkinter import *
from tkinter import ttk


class AppInterface:
    def __init__(self):
        # -------- Window arrangement ---------- #
        self.root = Tk()
        self.root.title("Gym Activity Tracker")
        self.root.config(pady=20, padx=20)
        self.root.minsize(700, 600)
        # -------- Tabs arrangement ------------ #
        self.style = ttk.Style().configure("Tabs style", padding=[12, 12], font=("Arial", 10))
        self.tab_control = ttk.Notebook(self.root, style="Tabs style")
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab1, text="Tab1")
        self.tab_control.add(self.tab2, text="Tab2")
        self.tab_control.pack(expand=1, fill="both")
        self.label1 = Label(self.tab1, text="Lets dive into the world of computers")
        self.label1.grid(row=0, column=0)
        self.label2 = Label(self.tab2, text="I'm number 2")
        self.label2.grid(row=0, column=0)

        self.root.mainloop()
    