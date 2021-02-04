from models.AccountHolder import AccountHolder
from typing import List


class AccountHolderManager:
    account_holders: List[AccountHolder] = []

    def register_account_holder(self, first_name: str, last_name: str, email: str, password: str, confirm_password: str,
                                phone_number: str):
        if password == confirm_password:
            owner_id = self.__get_id()
            owner = AccountHolder(id=owner_id, email=email,
                                  last_name=last_name, password=password)
            owner.first_name = first_name
            owner.phone_number = phone_number
            self.account_holders.append(owner)
            return owner
        else:
            return False

    def login(self, email: str, password: str):
        for account_holder in self.account_holders:
            if account_holder.email == email and account_holder.password == password:
                return account_holder
            else:
                return False

    def update_account_holder(self, email: str, first_name: str, last_name: str, phone_number: str):
        account_holder = self.__find(email=email)
        account_holder.phone_number = phone_number
        account_holder.first_name = first_name
        account_holder.last_name = last_name
        return True

    def change_password(self, email, password):
        account_holder = self.__find(email)
        if account_holder != None:
            account_holder.password = password
            return True
        else:
            return False

    def list_account_holders(self):
        for account_holder in self.account_holders:
            self.__show(account_holder)

    def search(self, email):
        account_holder = self.__find(email)
        if account_holder is None:
            return False
        else:
            self.__show(account_holder)

    def delete_account_holder(self, email: str):
        account_holder = self.__find(email)
        if account_holder is None:
            return False
        else:
            self.account_holders.remove(account_holder)
            return True

    def __get_id(self):
        length = len(self.account_holders)
        if length == 0:
            length += 1
            return length
        else:
            for account_holder in self.account_holders:
                if account_holder.id == length:
                    length += 1
                    return length

    def __find(self, email: str):
        for account_holder in self.account_holders:
            if account_holder.email == email:
                return account_holder
            else:
                return None

    def __show(self, account_holder: AccountHolder):
        print(account_holder.id, '\t', account_holder.first_name, '',
              account_holder.last_name, '\t', account_holder.email, '\t', account_holder.phone_number)
