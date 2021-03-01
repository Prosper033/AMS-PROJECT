from repositories.ManagerRepository import ManagerRepository
from models.Manager import Manager
from utils import *


class ManagerManagementService:
    manager_repository = ManagerRepository()
    logged_in_data = {}

    def create(self):
        first_name = prompt_for_non_empty_string("Enter your first name: ")
        last_name = prompt_for_non_empty_string("Enter your last name: ")
        phone_number = prompt_for_non_empty_string("Enter your Phone Number: ")
        email = prompt_for_non_empty_string("Enter your email: ")
        password = prompt_for_non_empty_string("Enter your password:")
        confirm_password = prompt_for_non_empty_string("Enter your password again: ")
        if password == confirm_password:
            manager = Manager(email=email, password=password, first_name=first_name, last_name=last_name,
                              phone_number=phone_number)
            self.manager_repository.create(manager)
            print("Account successfully created")
        else:
            print("password must match")

    def login(self):
        email = prompt_for_non_empty_string("Enter your email: ")
        password = prompt_for_non_empty_string("Enter your password: ")
        manager = self.manager_repository.find(email=email)
        if manager:
            if manager.password == password:
                print("login successful")
                return True
            else:
                print('password incorrect')
                return False
        else:
            print('account not found')
            return False

    def update(self):
        first_name = prompt_for_non_empty_string("Enter your first name: ")
        last_name = prompt_for_non_empty_string("Enter your last name: ")
        phone_number = prompt_for_non_empty_string("Enter your Phone Number: ")
        manager = Manager(first_name=first_name, last_name=last_name, phone_number=phone_number)
        self.manager_repository.update(manager=manager)

    def find(self):
        email = prompt_for_non_empty_string("Enter your email address: ")
        account_holder = self.manager_repository.find(email=email)
        print(account_holder)

    def delete(self):
        email = prompt_for_non_empty_string("Enter your email address: ")
        self.manager_repository.delete(email=email)
        print('Done')

    def list(self):
        account_holders = self.manager_repository.list()
        for account_holder in account_holders:
            print(account_holder)

    def change_password(self):
        email = prompt_for_non_empty_string("Enter your email: ")
        new_password = prompt_for_non_empty_string("Enter your new password:")
        self.manager_repository.change_password(email=email, new_password=new_password)
        print('Done')
