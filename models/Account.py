from models.AccountHolder import AccountHolder
import datetime


class Account:
    def __init__(self, account_holder: AccountHolder):
        self.account_holder = account_holder
        self.account_number = None
        self.account_type = None
        self.account_balance = 0
        self.date_of_creation = datetime.date.today()
        self.account_status = 'active'
