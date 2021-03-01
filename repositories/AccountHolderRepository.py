from typing import List

from repositories.BaseRepository import BaseRepository
from models.AccountHolder import AccountHolder


class AccountHolderRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.db = BaseRepository.db

    def create(self, account_holder: AccountHolder):
        cursor = self.db.cursor()
        sql = "INSERT INTO account_holder (first_name, last_name, email, phone_number) values (%s, %s, %s, %s)"
        val = (account_holder.first_name, account_holder.last_name, account_holder.email, account_holder.phone_number)
        cursor.execute(sql, val)
        self.db.commit()
        account_holder.id = cursor.lastrowid

    def find(self, email: str):
        cursor = self.db.cursor()
        sql = "SELECT first_name, last_name, phone_number FROM account_holder WHERE email = %s"
        val = (email,)
        cursor.execute(sql, val)
        record = cursor.fetchone()
        account_holder = AccountHolderRepository.__map_selected_record_to_account_holder(record)
        return account_holder

    def update(self, account_holder: AccountHolder):
        cursor = self.db.cursor()
        sql = "UPDATE account_holder SET first_name = %s, last_name = %s, phone_number = %s WHERE email = %s"
        val = (account_holder.first_name, account_holder.last_name, account_holder.phone_number)
        cursor.execute(sql, val)
        self.db.commit()

    def list(self):
        cursor = self.db.cursor()
        sql = "SELECT first_name, last_name, email, phone_number, FROM account_holder"
        cursor.execute(sql, )
        results = cursor.fetchall()
        account_holders: List[AccountHolder] = []
        for record in results:
            account_holder = AccountHolderRepository.__map_selected_record_to_account_holder(record)
            account_holders.append(account_holder)
        return account_holders


    @staticmethod
    def __map_selected_record_to_account_holder(record):
        if record is None:
            return None
        first_name, last_name, email, password, phone_number = record
        account_holder = AccountHolder(email=email, first_name=first_name, last_name=last_name,
                                        phone_number=phone_number)
        account_holder.id = id
        return account_holder
