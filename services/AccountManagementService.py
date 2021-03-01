import random

from repositories.AccountHolderRepository import AccountHolderRepository
from repositories.AccountRepository import AccountRepository
from models.AccountHolder import AccountHolder
from models.Account import Account
from utils import *


class AccountManagementService:
    account_holder_repository = AccountHolderRepository()
    account_repository = AccountRepository()

    def create(self, account_holder: AccountHolder):
        account_name = self.__get_account_name(account_holder=account_holder)
        account_number = self.__get_account_number()
        pin = prompt_for_valid_integer_input("Enter your four digit pin: ")
        balance = 0.0
        status = "active"
        account = Account(account_name=account_name, account_number=account_number, pin=pin, balance=balance,
                          status=status, account_holder_id=account_holder.id)
        self.account_repository.create(account=account)
        print(f"Account created successfully and your account number is {account_number}")

    def __get_account_name(self, account_holder: AccountHolder):
        last_name = account_holder.last_name
        first_name = account_holder.first_name
        account_name = last_name + " " + first_name
        return account_name

    def __get_account_number(self):
        code = "CODE"
        figure = str(random.randint(10000, 99999))
        account_number = code + figure
        return account_number

    def login(self):
        account_number = prompt_for_non_empty_string("Enter your account number: ")
        pin = prompt_for_valid_integer_input("Enter your pin: ")
        account_holder = self.account_repository.find(account_number=account_number)
        if account_holder:
            if account_holder.pin == pin:
                print("login successful")
                return True
            else:
                print("incorrect pin")
                return False
        else:
            print("create account with CODEBANK")
            return False

    def change_pin(self):
        account_number = prompt_for_non_empty_string("Enter your account number: ")
        account = self.account_repository.find(account_number=account_number)
        if account:
            pin = prompt_for_valid_integer_input("Enter your four digit pin: ")
            confirm_pin = prompt_for_valid_integer_input("Enter your four digit pin again: ")
            if pin == confirm_pin:
                new_pin = prompt_for_valid_integer_input("Enter your new four digit: ")
                self.account_repository.change_pin(account_number=account_number, new_pin=new_pin)
                print("Pin changed successfully")
                return True
            else:
                print("pin must match")
        else:
            print("account not found")

    def deposit(self):
        destination_account_number = prompt_for_non_empty_string("Enter your account number: ")
        account = self.account_repository.find_destination(account_number=destination_account_number)
        if account:
            amount = prompt_for_valid_integer_input("Enter amount to deposit: ")
            new_balance = account.balance + amount
            self.account_repository.deposit_or_withdraw(account_number=destination_account_number,
                                                        new_balance=new_balance)
            print(f"transaction successful and your new account balance is {new_balance}NGR")
        else:
            print("account not found with CODEBANK")

    def withdraw(self):
        account_number = prompt_for_non_empty_string("Enter your account number: ")
        account = self.account_repository.find(account_number)
        if account:
            if account.status == "active":
                amount = prompt_for_valid_integer_input("Enter amount to withdraw: " '\n')
                if amount < account.balance:
                    new_balance = account.balance - amount
                    self.account_repository.deposit_or_withdraw(account_number=account.account_number,
                                                                new_balance=new_balance)
                    print("transaction successful")
                else:
                    print("insufficient balance")
            else:
                print("account blocked, see your account manager")
        else:
            print("account not found with CODEBANK")

    def transfer(self):
        account_number = prompt_for_non_empty_string("Enter your account number: ")
        destination_account_number = prompt_for_non_empty_string("Enter the destination account_number: ")
        source = self.account_repository.find(account_number=account_number)
        destination = self.account_repository.find_destination(account_number=destination_account_number)
        if source and destination:
            if source.status == "active":
                amount = prompt_for_valid_integer_input("Enter the amount you want to transfer: ")
                if amount <= source.balance:
                    source_new_balance = source.balance - amount
                    self.account_repository.deposit_or_withdraw(account_number=account_number,
                                                                new_balance=source_new_balance)
                    destination_new_balance = destination.balance + amount
                    self.account_repository.deposit_or_withdraw(account_number=destination_account_number,
                                                                new_balance=destination_new_balance)
                    print("transaction successful")
                else:
                    print("insufficient balance")
            else:
                print("contact your account manager!")
        else:
            print('account details not found')

    def account_balance(self):
        account_number = prompt_for_non_empty_string("Enter your account number: ")
        account = self.account_repository.find(account_number=account_number)
        if account:
            print(f"Your account balance is {account.balance}NGR")
        else:
            print("account not found")

    def block_account(self):
        account_number = prompt_for_non_empty_string("Enter the account number: ")
        account = self.account_repository.find(account_number=account_number)
        if account:
            if account.status == "active":
                new_status = "inactive"
                self.account_repository.block_unblock(account_number=account_number, new_status=new_status)
                print("account blocked")
        else:
            print("account not found")

    def unblock_account(self):
        account_number = prompt_for_non_empty_string("Enter the account number: ")
        account = self.account_repository.find(account_number=account_number)
        if account:
            if account.status == "inactive":
                new_status = "active"
                self.account_repository.block_unblock(account_number=account_number, new_status=new_status)
                print("account unblocked")
        else:
            print("account not found")

    def list_accounts(self):
        accounts = self.account_repository.list_accounts()
        for account in accounts:
            print(account)
