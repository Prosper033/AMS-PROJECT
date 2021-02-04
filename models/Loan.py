from models.Account import Account
import datetime


class Loan:
    def __init__(self, account: Account, loan_type: str):
        self.account = account
        self.loan_type = loan_type
        self.interest_rate = None
        self.loan_date = datetime.date.today()
        self.loan_amount = 0.0
        self.balance = 0.0
        self.status = "inactive"
        self.id = 0
