import os

def users_list_exists():
    if os.path.isfile("settings/users_list.csv"):
        print("Checking 'users_list.csv' file... Completed. File exists.")
    else:
        print("Checking 'users_list.csv' file...  File not found. Restoring.")
        with open("settings/users_list.csv", "w") as users_list:
            users_list.write("id,name,password\n")