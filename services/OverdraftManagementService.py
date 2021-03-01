from models.Overdraft import Overdraft
from repositories.OverdraftRepository import OverdraftRepository
from utils import *
from repositories .AccountRepository import AccountRepository


class OverdraftManagementService:
    overdraft_repository = OverdraftRepository()
    account_repository = AccountRepository()

    def create_overdraft(self):
        account_number = prompt_for_non_empty_string("Enter your account number: " '\n')
        pin = prompt_for_valid_integer_input("Enter your pin: " '\n')
        account = self.account_repository.find(account_number=account_number)
        if account and account.pin == pin:
            amount = prompt_for_valid_integer_input("How much do you want to collect as overdraft?"
                                                    " (You cannot collect more than 100000)" '\n')
            if amount < 100000:
                balance = amount
                overdraft = Overdraft(amount=amount, balance=balance, account=account.account_number)
                overdraft.overdraft_status = 'active'
                overdraft = self.overdraft_repository.create(overdraft=overdraft)
                if overdraft:
                    print('OVERDRAFT COLLECTED SUCCESSFULLY' '\n')
                else:
                    print('OVERDRAFT UNSUCCESSFUL' '\n')
            else:
                print('AMOUNT GREATER THAN 100000' '\n')
        else:
            print('ACCOUNT NOT FOUND. INPUT THE CORRECT DETAILS AND TRY AGAIN.' '\n')

    def list(self):
        overdrafts = self.overdraft_repository.list()
        for overdraft in overdrafts:
            self.__show(overdraft)

    def __show(self, overdraft: Overdraft):
        print(f"""OVERDRAFT ID: {overdraft.id}\t DATE COLLECTED: {overdraft.date_created}\t 
              OVERDRAFT BALANCE: {overdraft.balance}\n""")

    def show_overdraft_balance(self):
        account_number = prompt_for_non_empty_string( "Enter your account number: " '\n')
        account = self.account_repository.find(account_number=account_number)
        pin = prompt_for_valid_integer_input("Enter your pin: " '\n')
        if account and account.pin == pin:
            overdraft = self.overdraft_repository.find(account=account_number)
            if overdraft:
                print(f"""YOUR OVERDRAFT BALANCE IS {overdraft.balance}\n""")
            else:
                print('YOU HAVE NO OVERDRAFT TO PAY' '\n')
        else:
            print('ACCOUNT NOT FOUND' '\n')

