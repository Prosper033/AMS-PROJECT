from models.Account import Account
import datetime


class Overdraft:
    def __init__(self, account: Account, amount: float):
        self.account = account
        self.amount = amount
        self.date = datetime.date.today()
