from core.security import Security
from core.ui import MainInterface
from core.system_scripts import users_list_exists


def main():
    users_list_exists() # performing a check of existing the users list file
    authorization = Security()
    authorization.run()
    if authorization.security_passed:
        print("Authorization SUCCESS")
        app = MainInterface(authorization.user_name.get())







if __name__ == '__main__':
    main()