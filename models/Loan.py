import datetime


class Loan:
    id: int
    account_number: str
    loan_type: str
    amount: float
    rate: float
    months: int
    balance: float
    status: str
    loan_date = datetime

    def __init__(self, loan_type: str, account_number="",  amount=0.0, rate=0.0, months=0, balance=0.0,
                 status="inactive", loan_date=datetime.date.today()):
        self.account_number = account_number
        self.loan_type = loan_type
        self.amount = amount
        self.rate = rate
        self.months = months
        self.balance = balance
        self.status = status
        self.loan_date = loan_date

    def __str__(self):
        return f"{self.id}\t{self.loan_type}\t{self.amount}\t{self.rate}\t{self.months}\t{self.balance}\t{self.status}\t{self.loan_date}"

