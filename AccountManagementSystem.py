from models.AccountHolder import AccountHolder
from models.Manager import Manager
from managers.ManagersManager import ManagersManager
from managers.AccountHolderManager import AccountHolderManager

account_holder_manager = AccountHolderManager()
manager_system = ManagersManager()


def main_menu():
    print("""Welcome to CodeBank
    Enter 1 to Access Account Holder Menu
    Enter 2 to Access Manager Menu
    Enter 0 to Quit
    -->""")


def sub_menu(option):
    if option == 0:
        print("Thank you for using CodeBank")
    elif option == 1:
        holder_register_login_menu()
        action = int(input())
        if action == 0:
            main_menu()
        else:
            holder_sub_menu(action)
    elif option == 2:
        manager_register_login_menu()
        action = int(input())
        if action == 0:
            main_menu()
        else:
            manager_sub_menu(option)


def holder_register_login_menu():
    print("""Account Holder Menu:
    Enter 1 to create account
    Enter 2 to login
    Enter 0 to go back
    -->""")


def manager_register_login_menu():
    print("""Account Holder Menu:
    Enter 1 to create account
    Enter 2 to login
    Enter 0 to go back
    -->""")


def holder_sub_menu(action):
    if action == 0:
        main_menu()
    elif action == 1:
        first_name = str(input("Enter your first name: "))
        middle_name = str(input("Enter your middle_name: "))
        last_name = str(input("Enter your last name: "))
        email = str(input("Enter your email address: "))
        password = str(input("Enter your password: "))
        confirm_password = str(input("Enter your password again: "))
        phone_number = str(input("Enter your phone number: "))
        holder = account_holder_manager.register_account_holder(
            email=email, password=password, confirm_password=confirm_password, first_name=first_name,
            middle_name=middle_name, last_name=last_name, phone_number=phone_number)
        if holder is True:
            print("You have successfully registered your account")
        else:
            print("Password must match")
    elif action == 2:
        email = str(input("Enter your email address: "))
        password = str(input("Enter your password: "))
        login = account_holder_manager.login(email=email, password=password)
        if login is False:
            print('Incorrect password')
        else:
            show_account_holder_menu()
            action = int(input())
            if action == 0:
                holder_register_login_menu()
            else:
                handle_account_holder_menu(action)

    sub_menu(1)


def manager_sub_menu(option):
    if option == 0:
        main_menu()
    elif option == 1:
        first_name = str(input("Enter your first name: "))
        middle_name = str(input("Enter your middle_name: "))
        last_name = str(input("Enter your last name: "))
        email = str(input("Enter your email address: "))
        password = str(input("Enter your password: "))
        confirm_password = str(input("Enter your password again: "))
        phone_number = str(input("Enter your phone number: "))
        holder = account_holder_manager.register_account_holder(
            email=email, password=password, confirm_password=confirm_password, first_name=first_name,
            middle_name=middle_name, last_name=last_name, phone_number=phone_number)
        if holder is False:
            print("incorrect password")
        else:
            account_manager.create

    elif option == 2:
        email = str(input("Enter your email address: "))
        password = str(input("Enter your password: "))
        login = manager_system.login(email=email, password=password)
        if login is True:
            show_manager_menu()
            action = int(input())
            if action == 0:
                manager_register_login_menu()
            else:
                handle_manager_menu(action)

    sub_menu(2)

def show_account_holder_menu():
    print("""Account Holder Menu:
    Enter 1 to update details
    Enter 2 to change password
    Enter 0 to go back
    -->""")


def show_manager_menu():
    print("""Manager Menu:
    Enter 1 to update manager details
    Enter 2 to change password
    Enter 3 to list account holders
    Enter 4 to search account holder
    Enter 5 to delete an account holder
    Enter 0 to go back
    -->""")


def handle_account_holder_menu(action):
    if action == 1:
        first_name = str(input("Enter new first name: "))
        middle_name = str(input("Enter new middle_name: "))
        last_name = str(input("Enter new last_name: "))
        phone_number = str(input("Enter new phone number: "))
        email = str(input())
        new_holder = account_holder_manager.update_account_holder
        if new_holder is True:
            print('Update valid')
        else:
            print('Update Invalid')

    elif action == 2:
        email = str(input("Enter your email address: "))
        password = str(input("Enter your password: "))
        status = account_holder_manager.change_password(
            email=email, password=password)
        if status is True:
            print("Password Changed")
        else:
            print("Password not valid")

    holder_sub_menu(1)


def handle_manager_menu(action):
    if action == 1:
        print("Log in your details")
        email = str(input("Enter your email address: "))
        password = str(input("Enter your password: "))
        manager = manager_system.login(email=email, password=password)
        if manager is False:
            print("Email or password incorrect")
        else:
            print("Update your profile")
            first_name = str(input("Enter your first name: "))
            middle_name = str(input("Enter your middle name: "))
            last_name = str(input("Enter your last_name: "))
            phone_number = str(input("Enter your phone number: "))
            new_manager = manager_system.update_manager(first_name=first_name, middle_name=middle_name,
                                                        last_name=last_name, email=email, phone_number=phone_number)
            if new_manager is True:
                print('Update valid')
            else:
                print('Update Invalid')

    elif action == 2:
        email = str(input("Enter your email address: "))
        password = str(input("Enter your password: "))
        login = manager_system.login(email=email, password=password)
        if login is True:
            new_password = str(input("Enter your new password: "))
            manager_system.change_password(new_password=new_password)
            print("Password Changed")
        else:
            print("Password not valid")

    elif action == 3:
        print("Only Manager has access to this")
        manager_email = str(input("Enter your email address: "))
        manager_password = str(input("Enter your password: "))
        login = manager_system.login(email=manager_email, password=manager_password)
        if login is True:
            account_holder_manager.list_account_holders()
        else:
            print('wrong password')

    elif action == 4:
        print("Only Manager has Access to this")
        manager_email = str(input("Enter your email address: "))
        manager_password = str(input("Enter your password: "))
        login = manager_system.login(email=manager_email, password=manager_password)
        if login is True:
            email = str(input("Enter the email of the account holder: "))
            account_holder_manager.search(email=email)
            print('Not Found')

    elif action == 5:
        email = str(input("Enter your email address: "))
        password = str(input("Enter your password: "))
        holder = account_holder_manager.login(email=email, password=password)
        if holder is False:
            print("Incorrect Password")
        else:
            status = account_holder_manager.delete_account_holder(email=email)
            if status is True:
                print("Account Deleted")
            else:
                print("Account not deleted")

    manager_sub_menu(2)


def main():
    flag = True
    while (flag):
        main_menu()
        option = int(input())
        if (option == 0):
            flag = False
        else:
            sub_menu(option)

main()
