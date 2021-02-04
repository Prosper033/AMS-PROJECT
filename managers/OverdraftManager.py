import datetime
from typing import List

from models.Overdraft import Overdraft
from models.Account import Account


class OverdraftManager:
    overdrafts: List[Overdraft] = []

    message = {}

    def get_overdraft(self, account: Account, amount):
        active_account = self.__is_account_active(account)
        if active_account is True:
            if amount <= 100000:
                overdraft_inactive = self.__is_overdraft_inactive(account=account)
                if overdraft_inactive is True:
                    overdraft = Overdraft(account=account, amount=amount)
                    overdraft.id = self.__get_id()
                    overdraft.balance = account
                    overdraft.account.account_balance -= amount
                    overdraft.date = datetime.date.today()
                    self.overdrafts.append(overdraft)
                    self.message['message'] = 'Overdraft granted, Your overdraft balance is', overdraft.balance
                    return self.message
                else:
                    self.message['pay_up'] = 'You still have unpaid overdraft, kindly pay up!'
                    return self.message
            else:
                self.message['much'] = 'You cannot get more than 100000 Naira'
                return self.message
        else:
            self.message['see_manager'] = 'Your account is blocked, kindly visit your account manager!'
            return self.message

    def pay_overdraft(self, account_number: str, amount: float):
        overdraft = self.__get_overdraft(account_number=account_number)
        if overdraft is not False:
            overdraft.balance -= amount
            if overdraft.balance == 0:
                overdraft.status = 'inactive'
                self.message['pay'] = 'Loan Totally paid'
                return self.message
            else:
                self.message['pay_success'] = 'Payment successful, yu have ', overdraft.balance, 'left to pay'
                return self.message
        else:
            self.message['not_found'] = 'No active loan found'

    def search_overdraft(self, account_number: str):
        for overdraft in self.overdrafts:
            if overdraft.account.account_number == account_number:
                return overdraft
            else:
                return False

    def list_overdraft(self):
        for overdraft in self.overdrafts:
            self.__show_loans(overdraft)

    def __show_overdrafts(self, overdraft: Overdraft):
        print(overdraft.id, '\t', overdraft.account.account_number, '\t', overdraft.status, '\t', overdraft.balance)

    def __get_overdraft(self, account_number: str):
        for overdraft in self.overdrafts:
            if overdraft.account.account_number == account_number:
                if overdraft.status == 'inactive':
                    return overdraft
                else:
                    return False

    def __is_account_active(self, account: Account):
        if account.account_status == "active":
            return True
        else:
            return False

    def __is_overdraft_inactive(self, account_number: str):
        for overdraft in self.overdrafts:
            if overdraft.account.account_number == account_number:
                if overdraft.status == "inactive":
                    return True
                else:
                    return False

    def __get_id(self):
        length = len(self.overdrafts)
        if length == 0:
            length += 1
            return length
        else:
            for overdraft in self.overdrafts:
                if overdraft.id == length:
                    length += 1
                    return length
                else:
                    continue
