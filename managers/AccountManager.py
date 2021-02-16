import random

from models.Account import Account
from models.AccountHolder import AccountHolder
from typing import List


class AccountManager():
    accounts: List[Account] = []

    file = open("Account.txt", "a+")

    def __init__(self):
        self.file.seek(0)
        for account_line in self.file:
            self.accounts.append(Account.parse(account_line))

    def create_account(self, account_holder: AccountHolder, pin: int):
        id = self.__get_id()
        accounts = Account(account_holder=account_holder, pin=pin, id=id)
        accounts.account_number = self.__get_account_number()
        accounts.account_name = self.__get_account_name(account_holder=account_holder)
        self.accounts.append(accounts)
        if self.file.closed is True:
            self.file = open("Account.txt", "a+")
        else:
            self.file.write(f"{str(accounts)}""\n")
            self.file.flush()

        return accounts.account_number

    def deposit(self, pin: int, amount: float, account_number: str):
        account = self.__get_account(account_number=account_number)
        if account:
            if account.pin == pin:
                account.account_balance += amount
                self.__refresh_file()
                return True
            else:
                return False
        else:
            return False

    def withdraw(self, pin: int, amount: float, account_number: str):
        account = self.__get_account(account_number=account_number)
        if account:
            if account.pin == pin and amount <= account.account_balance:
                if account.account_status == 'active':
                    account.account_balance -= amount
                    message = 'Done'
                    return message
                else:
                    message = 'not active, contact manager'
                    return message
            else:
                if account.account_balance < amount:
                    message = 'Insufficient funds'
                    return message
                else:
                    message = 'Incorrect Pin'
                    return message
        else:
            message = 'Account not found'
            return message

    def block_account(self, account_number):
        account = self.__get_account(account_number=account_number)
        account.account_status = 'inactive'
        self.__refresh_file()
        return True

    def unblock_account(self, account_number):
        account = self.__get_account(account_number=account_number)
        account.account_status = 'active'
        self.__refresh_file()
        return True

    def return_account(self, account_number: str, pin: int):
        account = self.__get_account(account_number=account_number)
        if account:
            if account.pin == pin:
                return account
            else:
                return False
        else:
            return False

    def change_pin(self, account_number: str, pin: int, new_pin: int):
        account = self.__get_account(account_number=account_number)
        if account:
            if account.pin == pin:
                account.pin = new_pin
                self.__refresh_file()
                return True
            else:
                return False
        else:
            return False

    def account_balance(self, account_number: str):
        account = self.__get_account(account_number=account_number)
        if account:
            self.__show_account_balance(account=account)
        else:
            answer = 'You have no account balance'
            return answer

    def __find(self, account_number: str):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
            else:
                return None

    def __get_id(self):
        length = len(self.accounts)
        if length == 0:
            length += 1
            return length
        else:
            for account_holder in self.accounts:
                if account_holder.id == length:
                    length += 1
                    return length
                else:
                    continue

    def __show_account_balance(self, account: Account):
        print('Your account balance is: ', account.balance)

    def __refresh_file(self):
        self.file = open("Account.txt", "w")
        for account in self.accounts:
            self.file.write(str(account))
            self.file.write("\n")
        self.file.flush()

    def __get_account(self, account_number: str):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return False

    def __get_receiver_account(self, receiver_account: str):
        for account in self.accounts:
            if account.account_number == receiver_account:
                return account
        return False

    @staticmethod
    def __get_account_number():
        code = '001023'
        digit = str(random.randint(1000, 9999))
        account_number = code + digit
        return account_number

    def __get_account_name(self, account_holder: AccountHolder):
        first_name = account_holder.first_name
        last_name = account_holder.last_name
        account_name = first_name + "" + last_name
        return account_name
