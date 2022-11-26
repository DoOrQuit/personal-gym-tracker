from tkinter import *
from tkinter import ttk
from datetime import date


class MainInterface:
    def __init__(self, current_user):
        self.current_user = current_user
        # -------- Window arrangement ---------- #
        self.root = Tk()
        self.root.title("Gym Activity Tracker")
        self.root.minsize(900, 520)
        self.root.config(padx=15, pady=15)
        # ----------------------- Labels ------------------ #
        self.profile_photo = Label(text="PHOTO HERE").grid(row=1, column=0, columnspan=2, pady=(20,40))
        self.user_logged = Label(text=f"{self.current_user}").grid(row=2, column=0, columnspan=2, pady=(0, 20))
        self.body_params = Label(text="BODY PARAMETERS :").grid(row=3, column=0, columnspan=2, pady=(0, 15))
        self.weight = Label(text="Weight (kg) :").grid(column=0, row=4, pady=15)
        self.shoulders_dia = Label(text="Shoulders (DIA, cm) :").grid(column=0, row=5, pady=15)
        self.biceps_dia = Label(text="Biceps (DIA, cm) :").grid(column=0, row=6, pady=15)
        self.stomack_dia = Label(text="Stomack (DIA, cm) :").grid(column=0, row=7, pady=15)
        self.ass_dia = Label(text="Ass (DIA, cm) :").grid(column=0, row=8, pady=15)
        self.date = Label(text=f"Date : {date.today()}").grid(column=4, row=0, pady=15)
        # ----------------------- Entries ------------------ #
        self.weight_entry = Entry(width=8).grid(column=1, row=4, pady=15)
        self.shoulders_entry = Entry(width=8).grid(column=1, row=5, pady=15)
        self.biceps_entry = Entry(width=8).grid(column=1, row=6, pady=15)
        self.stomack_entry = Entry(width=8).grid(column=1, row=7, pady=15)
        self.ass_entry = Entry(width=8).grid(column=1, row=8, pady=15)
        # ----------------------- Tabs ------------------ #
        self.tab_control = ttk.Notebook(self.root)
        self.tab1 = ttk.Frame(self.tab_control)
        self.tab2 = ttk.Frame(self.tab_control)
        self.label1 = Label(self.tab1, text="Lets dive into the world of computers")
        self.label2 = Label(self.tab2, text="I'm number 2")
        self.tab_control.add(self.tab1, text="Exercises")
        self.tab_control.add(self.tab2, text="Program 1")
        self.tab_control.grid(row=1, column=2)
        self.label1.grid(column=0, row=0)
        self.label2.grid(column=0, row=0)
        # ----------------------- Buttons ------------------ #
        self.settings_button = Button(text="Settings", width=10, command=self.settings).grid(column=2, row=0)
        self.logout_button = Button(text="Logout", width=10).grid(column=3, row=0)
        self.trend_body_params = Button(text="Trend", width=10).grid(column=0, row=9, pady=10)
        self.update_body_params = Button(text="Update", width=10).grid(column=1, row=9, pady=10)


        self.root.mainloop()


    def settings(self):
        # ----------------------- Window Parameters ------------------ #
        settings_window = Tk()
        settings_window.title("Settings")
        settings_window.minsize(500, 300)
        # ------------------------ Settings' Tabs --------------------- #
        settings_tabs_control = ttk.Notebook(settings_window)

        global_settings_tab = ttk.Frame(settings_tabs_control)
        profile_settings_tab = ttk.Frame(settings_tabs_control)
        settings_tabs_control.add(global_settings_tab, text="Global Settings")
        settings_tabs_control.add(profile_settings_tab, text="Profile Settings")
        settings_tabs_control.grid(column=0, row=0)

        # ------------------------ GLOBAL SETTINGS ----------------------------- #
        # ------------------------ Global Settings' Labels --------------------- #
        lang_settings_label = Label(global_settings_tab, text="Interface Language: ")
        lang_settings_label.grid(column=0, row=0, padx=20, pady=20)

        # ------------------------ Global Settings' Buttons --------------------- #
        settings_apply_button = Button(global_settings_tab, text="Apply")
        settings_apply_button.grid(column=0, row=3)
        settings_cancel_button = Button(global_settings_tab, text="Cancel")
        settings_cancel_button.grid(column=1, row=3)

        # ------------------------ Global Settings' Dropdown Menus --------------------- #
        current_language_set = StringVar(global_settings_tab)
        current_language_set.set("english")
        settings_language_options = OptionMenu(global_settings_tab, current_language_set, "english", "українська")
        settings_language_options.grid(column=1, row=0)

        # ------------------------ PROFILE SETTINGS ----------------------------- #
        # ------------------------ Profile Settings' Labels --------------------- #
        profile_name_change_label = Label(profile_settings_tab, text="Profile Name", padx=20, pady=20)
        profile_name_change_label.grid(column=0, row=0)
        profile_pass_change_label = Label(profile_settings_tab, text="")










