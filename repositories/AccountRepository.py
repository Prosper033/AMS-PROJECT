from typing import List

from repositories.BaseRepository import BaseRepository
from models.Account import Account


class AccountRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.db = BaseRepository.db

    def create(self, account: Account):
        cursor = self.db.cursor()
        sql = "INSERT INTO account (account_holder_id, account_name, account_number, pin, balance, status) values (%s, %s, %s, %s, %s, %s)"
        val = (account.account_holder_id, account.account_name, account.account_number, account.pin, account.balance,
               account.status)
        cursor.execute(sql, val)
        self.db.commit()
        account.id = cursor.lastrowid

    def find(self, account_number: str):
        cursor = self.db.cursor()
        sql = "SELECT account_holder_id, account_name, pin, balance, status FROM account WHERE account_number = %s"
        val = (account_number,)
        cursor.execute(sql, val)
        record = cursor.fetchone()
        account = AccountRepository.__map_selected_record_to_account(record)
        return account

    def find_destination(self, account_number: str):
        cursor = self.db.cursor()
        sql = "SELECT account_holder_id, account_name, pin, balance, status FROM account WHERE account_number = %s"
        val = (account_number,)
        cursor.execute(sql, val)
        record = cursor.fetchone()
        receiver_account = AccountRepository.__map_selected_record_to_account(record)
        return receiver_account

    def list_accounts(self):
        cursor = self.db.cursor()
        sql = "SELECT account_name, account_number, pin, balance, status FROM account"
        cursor.execute(sql, )
        results = cursor.fetchall()
        accounts: List[Account] = []
        for record in results:
            account = AccountRepository.__map_selected_record_to_account(record)
            accounts.append(account)
        return accounts

    def deposit_or_withdraw(self, account_number: str, new_balance: float):
        cursor = self.db.cursor()
        sql = "UPDATE account SET balance = %s WHERE account_number = %s"
        val = (new_balance, account_number)
        cursor.execute(sql, val)
        self.db.commit()

    def change_pin(self, account_number: str, new_pin: int):
        cursor = self.db.cursor()
        sql = "UPDATE account SET pin = %s WHERE account_number = %s"
        val = (new_pin, account_number)
        cursor.execute(sql, val)
        self.db.commit()

    def block_unblock(self,account_number: str, new_status:str):
        cursor = self.db.cursor()
        sql = "UPDATE account SET status = %s WHERE account_number = %s"
        val = (new_status, account_number)
        cursor.execute(sql, val)
        self.db.commit()

    @staticmethod
    def __map_selected_record_to_account(record):
        if record is None:
            return None
        account_name, account_number, pin, balance, status = record
        account = Account(account_name=account_name, account_number=account_number, pin=pin, balance=balance,
                          status=status)
        account.id = id
        return account
