from models.Account import Account
import datetime


class Loan:
    def __init__(self, account: Account, loan_type: str, amount="0.0", interest_rate="0.0", balance="0.0", status="inactive", date=datetime):
        self.account = account
        self.loan_type = loan_type
        self.id = 0
        self.amount = amount
        self.interest_rate = interest_rate
        self.balance = balance
        self.status = status
        self.date = date

    def __str__(self):
        return f"{self.id}\t{self.account}\t{self.loan_type}\t{self.amount}\t{self.interest_rate}\t{self.balance}\t{self.status}\t{self.date}"

    def parse(line: str):
        id, account, interest_rate, date, loan_type, balance, amount, status = line.split('\t')
        id = int(id)
        return Loan(account=account, loan_type=loan_type, amount=amount, interest_rate=interest_rate, balance=balance, status=status, date=date)


