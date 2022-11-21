from tkinter import *
from tkinter import ttk


class MainInterface:
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
        self.canvas.grid(column=0, row=0, rowspan=3)

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




