from services.AccountHolderManagementService import AccountHolderManagementService
from services.ManagerManagementService import ManagerManagementService
from services.AccountManagementService import AccountManagementService
from services.LoanManagementService import LoanManagementService
from services.OverdraftManagementService import OverdraftManagementService

account_holder_management_service = AccountHolderManagementService()
manager_management_service = ManagerManagementService()
account_management_service = AccountManagementService()
loan_management_service = LoanManagementService()
overdraft_management_service = OverdraftManagementService()


def main_menu():
    print("""Welcome to CodeBank
    Enter 1 to Access Account Holder Menu
    Enter 2 to Access Manager Menu
    Enter 0 to Quit
    -->""")


def sub_menu(option):
    if option == 1:
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
            manager_sub_menu(action)


def holder_register_login_menu():
    print("""Account Holder Menu:
    Enter 1 to create bank account
    Enter 2 to login account holder
    Enter 0 to go back
    -->""")


def manager_register_login_menu():
    print("""Manager Menu:
    Enter 1 to create manager account
    Enter 2 to login manager
    Enter 0 to go back
    -->""")


def holder_sub_menu(action):
    if action == 1:
        print("REGISTER ACCOUNT HOLDER")
        account_holder = account_holder_management_service.create()
        account_management_service.create(account_holder=account_holder)
        holder_register_login_menu()
        action = int(input())
        holder_sub_menu(action)
    elif action == 2:
        print("ACCOUNT HOLDER LOGIN")
        login = account_management_service.login()
        if login:
            show_holder_menu()
            action = int(input())
            handle_holder_menu(action)
        else:
            sub_menu(1)


def manager_sub_menu(option):
    if option == 1:
        print("REGISTER MANAGER")
        manager_management_service.create()
        manager_register_login_menu()
        action = int(input())
        manager_sub_menu(action)
    elif option == 2:
        print("MANAGER LOGIN")
        login = manager_management_service.login()
        if login:
            show_manager_menu()
            action = int(input())
            handle_manager_menu(action)
        else:
            sub_menu(2)


def show_holder_menu():
    print("""Account Holder Menu:
    Enter 1 for account transactions
    Enter 2 to loan transactions
    Enter 3 to overdraft transactions
    Enter 0 to go back
    -->""")


def show_manager_menu():
    print("""Manager Menu:
    Enter 1 for account transactions
    Enter 2 to loan transactions
    Enter 3 to overdraft transactions
    Enter 0 to go back
    -->""")


def handle_holder_menu(action):
    if action == 1:
        holder_account_menu()
        action = int(input())
        if action == 0:
            holder_register_login_menu()
        else:
            handle_holder_account_menu(action)
    if action == 2:
        holder_loan_menu()
        action = int(input())
        if action == 0:
            holder_register_login_menu()
        else:
            handle_holder_loan_menu(action)
    if action == 3:
        holder_overdraft_menu()
        action = int(input())
        if action == 0:
            holder_register_login_menu()
        else:
            handle_holder_overdraft_menu(action)


def handle_manager_menu(action):
    if action == 1:
        manager_account_menu()
        action = int(input())
        if action == 0:
            manager_register_login_menu()
        else:
            handle_manager_account_menu(action)

    if action == 2:
        manager_loan_menu()
        action = int(input())
        if action == 0:
            manager_register_login_menu()
        else:
            handle_manager_loan_menu(action)
    if action == 3:
        manager_overdraft_menu()
        action = int(input())
        if action == 0:
            manager_register_login_menu()
        else:
            handle_manager_overdraft_menu(action)


def holder_account_menu():
    print("""Account Holder: Account:
    Enter 1 to update details
    Enter 2 to change pin
    Enter 3 to make deposit
    Enter 4 to make withdrawal
    Enter 5 to make transfer
    Enter 6 to check balance
    Enter 0 to go back
    -->""")


def holder_loan_menu():
    print("""Account Holder: Loan:
    Enter 1 to obtain a loan
    Enter 2 to check loan balance
    Enter 3 to pay back a loan
    Enter 0 to go back
    -->""")


def holder_overdraft_menu():
    print("""Account Holder: Overdraft:
    Enter 1 to get overdraft
    Enter 0 to go back
    -->""")


def manager_account_menu():
    print("""Manager: Account:
    Enter 1 to update manager details
    Enter 2 to change password
    Enter 3 to list account holders
    Enter 4 to search account holder
    Enter 5 to block an account
    Enter 6 to unblock an account
    Enter 0 to go back
    -->""")


def manager_loan_menu():
    print("""Manager: Loan:
    Enter 1 to search loans
    Enter 2 to list loans
    Enter 0 to go back
    -->""")


def manager_overdraft_menu():
    print("""Manager: Overdraft:
    Enter 1 to search overdraft
    Enter 2 to list overdraft
    Enter 0 to go back
    -->""")


def handle_holder_account_menu(action):
    if action == 1:
        print("UPDATE ACCOUNT HOLDER DETAILS")
        account_holder_management_service.update()

    elif action == 2:
        print("CHANGE PIN")
        account_management_service.change_pin()

    elif action == 3:
        print("DEPOSIT")
        account_management_service.deposit()

    elif action == 4:
        print("WITHDRAWAL")
        account_management_service.withdraw()

    elif action == 5:
        print("TRANSFER")
        account_management_service.transfer()

    elif action == 6:
        print("CHECK BALANCE")
        account_management_service.account_balance()

    holder_account_menu()
    action = int(input())
    if action == 0:
        holder_register_login_menu()
    else:
        handle_manager_overdraft_menu(action)


def handle_holder_loan_menu(action):
    if action == 1:
        print("GET LOAN")
        loan_management_service.create_loan()

    elif action == 2:
        print("PAY LOAN")
        loan_management_service.pay_back()


def handle_holder_overdraft_menu(action):
    if action == 1:
        print("GET OVERDRAFT")
        overdraft_management_service.create_overdraft()



def handle_manager_account_menu(action):
    if action == 1:
        print("UPDATE  MANAGER DETAILS")
        new_manager = manager_management_service.update()
        if new_manager is True:
            print('Update valid')
        else:
            print('Update Invalid')

    elif action == 2:
        print("CHANGE MANAGER PASSWORD")
        change = manager_management_service.change_password()
        if change:
            print("Password Changed")
        else:
            print("Password not valid")

    elif action == 3:
        print("LIST OF ACCOUNT HOLDERS")
        account_holder_management_service.list()


def handle_manager_loan_menu(action):
    if action == 1:
        print("SEARCH FOR A LOAN")
        loan = loan_management_service.list()
        if loan is False:
            print("Wrong account number")
        else:
            print(loan.id, '\t', loan.status, '\t', loan.loan_type)

    elif action == 2:
        print("LIST OF LOANS")
        loan_manager.list_loan()


def handle_manager_overdraft_menu(action):
    if action == 1:
        print("SEARCH FOR OVERDRAFT")
        account_number = str(input("Enter the account number: "))
        overdraft = overdraft_manager.search_overdraft(account_number=account_number)
        if overdraft is False:
            print("Wrong account number")
        else:
            print(overdraft.id, '\t', overdraft.status, '\t', overdraft.balance)

    elif action == 2:
        print("LIST OF LOANS")
        overdraft_manager.list_overdraft()


def main():
    flag = True
    while (flag):
        main_menu()
        option = int(input())
        if option == 0:
            print("Thanks for banking with CodeBank!!")
            flag = False
        else:
            sub_menu(option)


main()
