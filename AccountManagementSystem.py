from models.AccountHolder import AccountHolder
from managers.AccountHolderManager import AccountHolderManager

account_holder_manager = AccountHolderManager()


def mainMenu():
    print("""weelcome to CodeBank
    Enter 0 to Quit
    Enter 1 to Access Account Holder Menu """)


def showMenu(option):
    if option == 0:
        print("Thank you for using CodeBank")
    elif option == 1:
        show_account_holder_menu
        action = int(input())
        if action == 0:
            mainMenu()
        else:
            handle_account_holder_menu(action)


def show_account_holder_menu():
    print("Enter 1 to create account" '\n' "Enter 2 to update details" '\n' "Enter 3 to change password" '\n' ")


def handle_account_holder_menu(action):
    if action == 1:
        email = str(input("Enter your email address: "))
        password = str(input("Enter your password: "))
        confirm_password = str(input("Enter your password: "))
        first_name = str(
            input("Enter your first name, else None will be used"))
        middle_name = str(
            input("Enter your middle_name, else None will be used"))
        last_name = str(
            input("Enter your last_name, else None will be used"))
        phone_number = str(
            input("Enter your phone number, else None will be used"))
        holder = account_holder_manager.create_account_holder(
            email=email, password=password, confirm_password=confirm_password, first_name=first_name, middle_name=middle_name, last_name=last_name, phone_number=phone_number)
        if holder is True:
            print("successful, your password is your first name")
        else:
            print("Password is incorrcet")

    elif action == 2:
        email = str(input("Enter your email address: "))
        password = str(input("Enter your password: "))
        holder = account_holder_manager.login(email=email, password=password)
        if holder is false:
            print("Email or password incorrect")
        else:
            first_name = str(
                input("Enter your first name, else None will be used"))
            middle_name = str(
                input("Enter your middle_name, else None will be used"))
            last_name = str(
                input("Enter your last_name, else None will be used"))
            phone_number = str(
                input("Enter your phone number, else None will be used"))
            new_holder = account_holder_manager.update_acount_holder(email, first_name=first_name, middle_name=middle_name, last_name=last_name, password)
            if new_holder is True:
                print('Update valid')
            else:
                print('Update Invalid')

    elif action == 3:
        email = str(input("Enter your email address: "))
        password = str(input("Enter your password: "))
        status = account_holder_manager.
