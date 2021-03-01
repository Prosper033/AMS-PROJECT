from typing import List
from repositories.BaseRepository import BaseRepository
from models.Loan import Loan


class LoanRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.db = BaseRepository.db

    def create(self, loan: Loan):
        cursor = self.db.cursor()
        sql = "INSERT INTO loan(account_number, loan_type, amount, rate, months, balance, status, loan_date) values (%s, %s, %s, %s, %s, %s, %s, %s)"
        val = (loan.account_number, loan.loan_type, loan.amount, loan.rate, loan.months, loan.balance, loan.status, loan.loan_date)
        cursor.execute(sql, val)
        self.db.commit()
        loan.id = cursor.lastrowid
        return loan.id

    def delete(self, account_number: str):
        cursor = self.db.cursor()
        sql = "DELETE FROM loan WHERE account_number=%s"
        val = (account_number,)
        cursor.execute(sql, val)
        self.db.commit()

    def find(self, account_number: str):
        cursor = self.db.cursor()
        sql = "SELECT loan_type, amount, rate, months, balance, status, loan_date FROM loan WHERE account_number = %s"
        val = (account_number,)
        cursor.execute(sql, val)
        record = cursor.fetchone()
        loan = LoanRepository.__map_selected_record_to_loan(record)
        return loan

    def list_loans(self):
        cursor = self.db.cursor()
        sql = "SELECT loan_type, amount, rate, balance, status, loan_date FROM loan"
        cursor.execute(sql, )
        results = cursor.fetchall()
        account_holders: List[Loan] = []
        for record in results:
            account_holder = LoanRepository.__map_selected_record_to_loan(record)
            account_holders.append(account_holder)
        return account_holders

    def show_loan_balance(self, account_number: str):
        cursor = self.db.cursor()
        sql = "SELECT loan_type, amount, rate, balance, status, loan_date FROM loan WHERE account_number = %s"
        val = (account_number,)
        cursor.execute(sql, val)
        record = cursor.fetchone()
        loan = LoanRepository.__map_selected_record_to_loan(record)
        return loan

    def update_loan_balance(self, account_number: str, balance: float):
        cursor = self.db.cursor()
        sql = "UPDATE loan SET balance = %s WHERE account_number = %s"
        val = (balance, account_number)
        cursor.execute(sql, val)
        self.db.commit()

    def update_loan_status(self, account_number: str, new_status: str):
        cursor = self.db.cursor()
        sql = "UPDATE loan SET loan_status = %s WHERE account_number = %s"
        val = (new_status, account_number)
        cursor.execute(sql, val)
        self.db.commit()
        return True

    @staticmethod
    def __map_selected_record_to_loan(record):
        if record is None:
            return None
        loan_type, amount, rate, months, balance, status, loan_date = record
        loan = Loan(loan_type=loan_type, amount=amount, rate=rate, months=months, balance=balance,
                    status=status, loan_date=loan_date)
        loan.id = id
        return loan
