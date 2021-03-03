from abc import abstractmethod, ABCMeta
from typing import List

from django.contrib.auth.models import User

from AMSapp.models import AccountHolder
from AMSapp.Dto.AccountHolderDto import *

class AccountHolderRepository(metaclass=ABCMeta):
    @abstractmethod
    def create_account_holder(self, model: RegisterAccountHolder):
        """Reister Account Holder Object"""
        raise NotImplementedError

    @abstractmethod
    def list_account_holder(self) -> List[ListAccountHolder]:
        """List Account Holder Object"""
        raise NotImplementedError

    @abstractmethod
    def account_holder_details(self, account_holder_id: int) -> AccountHolderDetails:
        """Return an Account Holder Object"""
        raise NotImplementedError

    @abstractmethod
    def edit_account_holder(self, account_holder_id: int, model: EditAccountHolder):
        """Edit an Account Holder Object"""
        raise NotImplementedError


class DjangoORMAccountHolderRepository(AccountHolderRepository):
    def create_account_holder(self, model: RegisterAccountHolder):
        account_holder = AccountHolder()
        user = User.objects.create_user(username=model.username, email=model.email, password=model.password)
        user.first_name = model.first_name
        user.last_name = model.last_name
        user.save()

        acc
