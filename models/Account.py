from models.AccountHolder import AccountHolder
import datetime


class Account:
    def __init__(self, account_holder: AccountHolder):
        self.account_owner = account_holder
        self.account_number = None
        self.account_type = account_type
        self.account_balance = 0
        self.date_of_creation = datetime.date.today()
        self.account_status = 'active'
