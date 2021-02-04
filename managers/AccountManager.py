import random

from models.Account import Account
from typing import List
from models.AccountHolder import AccountHolder


class AccountManager:

    accounts: List[Account] = []

    message = {}

    def create_account(self, account_holder: AccountHolder, pin: int):
        id = self.__get_id()
        accounts = Account(id=id, account_holder=account_holder, pin=pin)
        accounts.account_number = self.__get_account_number()
        self.accounts.append(accounts)
        return accounts

    def deposit(self, pin: int, amount: float, account_number: str):
        account = self.__get_account(account_number=account_number)
        if account is not None:
            if account.pin == pin:
                account.account_balance += amount
                return True
            else:
                return False
        else:
            return False

    def withdraw(self, pin: int, amount: float, account_number: str):
        account = self.__get_account(account_number=account_number)
        if account is not None:
            if account.pin == pin and amount <= account.account_balance:
                if account.account_status == 'active':
                    account.account_balance -= amount
                    self.message['message'] = 'Done'
                    return self.message
                else:
                    self.message['message'] = 'not active, contact manager'
                    return self.message
            else:
                if account.account_balance < amount:
                    self.message['message'] = 'Insufficient funds'
                    return self.message
                else:
                    self.message['message'] = 'Incorrect Pin'
                    return self.message
        else:
            self.message['message'] = 'Account not found'
            return self.message

    def block_account(self, account_number):
        account = self.__get_account(account_number=account_number)
        account.account_status = 'inactive'
        return True

    def unblock_account(self, account_number):
        account = self.__get_account(account_number=account_number)
        account.account_status = 'active'
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

    def __get_id(self):
        # gets the length of the account holder list and try to return the length + 1 as id if the account holder
        # list is not empty a private function
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

    def __get_account(self, account_number: str):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
            else:
                return False

    @staticmethod
    def __get_account_number():
        value = 'conk'
        digit = str(random.randint(1000, 9999))
        account_number = value.upper() + digit
        return account_number