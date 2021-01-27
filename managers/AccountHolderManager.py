from AccountHolder import AccountHolder


class AccountHolderManager:

    account_holders = []

    def create_account_holder(self, email: str, password: str, first_name: str, middle_name: str, last_name: str, phone_number: int):
        owner_id = self.__get_id
        owner = AccountHolder(id=owner_id, email=email,
                              last_name=last_name, password=password)
        return True

    def update_acount_holder(self, email: str, password: str, first_name: str, middle_name: str, last_name: str):
        account_holder = self.__find(email)
        if account_holder != None:
            account_holder.email = email
            account_holder.first_name = first_name
            account_holder.middle_name = middle_name
            account_holder.last_name = last_name
            return True
        else:
            return False

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

    def login(self, email: str, password: str):
        for account_holder in self.account_holders:
            if account_holder.email == email and account_holder.password == password:
                return account_holder
            else:
                return False

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
              account_holder.middle_name, '', account_holder.last_name, '\t', )
