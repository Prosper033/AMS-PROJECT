import datetime

class Overdraft:
    id: int
    account_id: int
    amount: float
    balance: float
    status: str
    overdraft_date: datetime

    def __init__(self, amount=0.0, balance=0.0, account=0, status="inactive", overdraft_date=datetime.date.today()):
        self.account = account
        self.amount = amount
        self.balance = balance
        self.status = status
        self.overdraft_date = overdraft_date

    def __str__(self):
        return f"{self.id}\t{self.amount}\t{self.balance}\t{self.status}\t{self.overdraft_date}"

