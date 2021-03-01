from repositories.AccountHolderRepository import AccountHolderRepository
from repositories.AccountRepository import AccountRepository
from repositories.LoanRepository import LoanRepository
from models.Loan import Loan
from utils import *
import mysql.connector


class LoanManagementService:
    loan_repository = LoanRepository()
    account_holder_repository = AccountHolderRepository()
    account_repository = AccountRepository()

    loan_types = ['household', 'car', 'school fee', 'business', 'emergency']
    loan_amount = [100000, 500000, 200000, 10000000, 50000]

    def create_loan(self):
        try:
            account_number = prompt_for_non_empty_string("Enter your account number: ")
            account = self.account_repository.find(account_number=account_number)
            if account.pin == pin:
                self.__print_loan()
                loan_type_choice = prompt_for_valid_integer_input("Enter your loan type: ")
                loan_type_details = self.__get_loan_amount_by_loan_type(loan_type_choice)
                loan_type = loan_type_details[0]
                amount = loan_type_details[1]
                number_of_months = prompt_for_valid_integer_input("Enter the number of months to pay back: ")
                interest_rate = self.__get_loan_interest_rate(number_of_months=number_of_months)
                balance = self.__get_loan_initial_balance(number_of_months=number_of_months, amount=amount)
                loan = Loan(loan_type=loan_type, amount=amount, balance=balance,
                            rate=interest_rate )
                loan.status = 'active'
                loan = self.loan_repository.create(loan)
                if loan:
                    print(f"Loan Granted. You have {balance} to pay")
                else:
                    print('Loan not granted!')
            else:
                print('wrong pin')
        except mysql.connector.errors.IntegrityError:
            print('Pay up pending loan')

    def pay_back(self):
        account_number = prompt_for_non_empty_string("Enter your account number: ")
        pin = prompt_for_valid_integer_input("Enter your pin: ")
        account = self.account_repository.find(account_number)
        if account and account.pin == pin:
            loan = self.loan_repository.find(account_number=account.account_number)
            if loan:
                payback_amount = prompt_for_valid_integer_input("Enter the amount you want to pay back: ")
                if loan.balance > payback_amount:
                    balance = loan.balance - payback_amount
                    self.loan_repository.update_loan_balance(account_number=account_number,
                                                             balance=balance)
                    print(f"LOAN PAYBACK SUCCESSFUL. YOU HAVE {balance} LEFT TO PAY")

                elif payback_amount == loan.balance:
                    balance = loan.balance - payback_amount
                    new_status = 'inactive'
                    self.loan_repository.update_loan_status(account_number=account_number,
                                                            new_status=new_status)
                    self.loan_repository.update_loan_balance(account_number=account.account_number,
                                                             balance=balance)
                    self.loan_repository.delete(loan_status=new_status)
                    print('LOAN TOTALLY PAID.' '\n')

                elif payback_amount < loan.balance:
                    payback_amount -= loan.balance
                    loan.balance = 0.0
                    account.balance += payback_amount
                    new_status = 'inactive'
                    self.loan_repository.update_loan_status(account_number=account_number,
                                                            new_status=new_status)
                    self.loan_repository.update_loan_balance(account_number=account.account_number,
                                                             balance=loan.balance)
                    self.loan_repository.delete(loan_status=new_status)
                    self.account_repository.deposit_or_withdraw(account_number=account_number,
                                                                new_balance=account.balance)
                    print('Loan Paid')
            else:
                print('YOU HAVE NO LOAN TO PAY UP FOR.' '\n')
        else:
            print('ACCOUNT NOT FOUND' '\n')

    def show_loan_balance(self):
        account_number = prompt_for_non_empty_string("Enter your account number: ")
        account = self.account_repository.find(account_number=account_number)
        pin = prompt_for_valid_integer_input("Enter your pin: ")
        if account and account.pin == pin:
            loan = self.loan_repository.find(account_number=account_number)
            if loan:
                print(f"""YOUR LOAN BALANCE IS {loan.balance}\n""")
            else:
                print('YOU HAVE NO PENDING LOAN BALANCE TO PAY UP FOR' '\n')
        else:
            print('ACCOUNT NOT FOUND' '\n')

    def __get_loan_initial_balance(self, number_of_months: int, amount: int):
        val = (number_of_months/12) * amount
        amount += val
        return amount

    def __get_loan_amount_by_loan_type(self, choice: int):
        loan_type_and_amount = []
        loan_type = self.loan_types[choice]
        amount = self.loan_amount[choice]
        loan_type_and_amount.append(loan_type)
        loan_type_and_amount.append(amount)
        return loan_type_and_amount

    def __get_loan_interest_rate(self, number_of_months: int):
        interest_rate = number_of_months / 12
        return interest_rate

    def list(self):
        loans = self.loan_repository.list()
        for loan in loans:
            self.__show(loan)

    def __print_loan(self):
        print("""Enter 0 for Household Loan: 1000000
        Enter 1 for Car Loan: 200000
        Enter 2 for School Loan: 500000
        Enter 3 for Business Loan: 1000000
        Enter 4 for Emergency Loan: 50000
        -->""")

    def __show(self, loan: Loan):
        print(f"{loan.id}\t{loan.loan_type}\t{loan.amount}{loan.balance}\t{loan.rate}\t{loan.rate}\t{loan.loan_date}")

