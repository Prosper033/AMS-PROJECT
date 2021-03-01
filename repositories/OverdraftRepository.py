from typing import List
from repositories.BaseRepository import BaseRepository
from models.Overdraft import Overdraft


class OverdraftRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.db = BaseRepository.db

    def create(self, overdraft: Overdraft):
        cursor = self.db.cursor()
        sql = "INSERT INTO overdraft (account_id, amount, balance, status, overdraft_date) values (%s, %s, %s, %s, %s)"
        val = (overdraft.id, overdraft.account, overdraft.amount,
               overdraft.overdraft_status, overdraft.balance)
        cursor.execute(sql, val)
        self.db.commit()
        overdraft.id = cursor.lastrowid
        return overdraft.id

    def delete(self, overdraft_status: str):
        cursor = self.db.cursor()
        sql = "DELETE FROM overdraft WHERE overdraft_status=%s"
        val = (overdraft_status,)
        cursor.execute(sql, val)
        self.db.commit()

    def find(self, account: int):
        cursor = self.db.cursor()
        sql = "SELECT id, account, amount, balance, status FROM overdraft WHERE account = %s"
        val = (account,)
        cursor.execute(sql, val)
        record = cursor.fetchone()
        overdraft = OverdraftRepository.__map_selected_record_to_overdraft(record)
        return overdraft

    def list(self):
        cursor = self.db.cursor()
        sql = "SELECT id, account, amount, overdraft_status, balance FROM overdraft"
        cursor.execute(sql, )
        results = cursor.fetchall()
        account_holders: List[Overdraft] = []
        for record in results:
            account_holder = OverdraftRepository.__map_selected_record_to_overdraft(record)
            account_holders.append(account_holder)
        return account_holders

    def show_overdraft_balance(self, account: int):
        cursor = self.db.cursor()
        sql = "SELECT id, account, amount, overdraft_status, balance FROM overdraft WHERE account = %s"
        val = (account,)
        cursor.execute(sql, val)
        record = cursor.fetchone()
        overdraft = OverdraftRepository.__map_selected_record_to_overdraft(record)
        return overdraft

    def update_overdraft_status(self, account: int, new_status: str):
        cursor = self.db.cursor()
        sql = "UPDATE overdraft SET overdraft_status = %s WHERE account = %s"
        val = (new_status, account)
        cursor.execute(sql, val)
        self.db.commit()
        return True

    def update_overdraft_balance(self, account: int, new_overdraft_balance: float):
        cursor = self.db.cursor()
        sql = "UPDATE overdraft SET balance = %s WHERE account = %s"
        val = (new_overdraft_balance, account)
        cursor.execute(sql, val)
        self.db.commit()

    def receiver_account_deposit(self, account_number: int, receiver_new_balance: float):
        cursor = self.db.cursor()
        sql = "UPDATE account SET balance = %s WHERE account_number = %s"
        val = (receiver_new_balance, account_number)
        cursor.execute(sql, val)
        self.db.commit()

    @staticmethod
    def __map_selected_record_to_overdraft(record):
        if record is None:
            return None
        id, account, amount, status, balance = record
        overdraft = Overdraft(account=account, amount=amount, status=status, balance=balance)
        overdraft.id = id
        return overdraft
