from repositories.AccountHolderRepository import AccountHolderRepository
from models.AccountHolder import AccountHolder
from utils import *


class AccountHolderManagementService:
    account_holder_repository = AccountHolderRepository()
    logged_in_data = {}

    def create(self):
        first_name = prompt_for_non_empty_string("Enter your first name: ")
        last_name = prompt_for_non_empty_string("Enter your last name: ")
        phone_number = prompt_for_non_empty_string("Enter your Phone Number: ")
        email = prompt_for_non_empty_string("Enter your email: ")
        account_holder = AccountHolder(first_name=first_name, last_name=last_name, email=email,
                                       phone_number=phone_number)
        self.account_holder_repository.create(account_holder)
        return account_holder

    def update(self):
        first_name = prompt_for_non_empty_string("Enter your first_name: ")
        last_name = prompt_for_non_empty_string("Enter your last name: ")
        phone_number = prompt_for_non_empty_string("Enter your Phone Number: ")
        email = prompt_for_non_empty_string("Enter your email: ")
        account_holder = AccountHolder(email=email, first_name=first_name, last_name=last_name,
                                       phone_number=phone_number)
        self.account_holder_repository.update(account_holder=account_holder)

    def find(self):
        email = prompt_for_non_empty_string("Enter your email address: ")
        account_holder = self.account_holder_repository.find(email=email)
        print(account_holder)

    def list(self):
        account_holders = self.account_holder_repository.list()
        for account_holder in account_holders:
            print(account_holder)
