from datetime import date


class RegisterAccountHolder:
    username: str
    first_name: str
    last_name: str
    email: str
    password: str
    confirm_password: str
    address: str
    phone_number: str
    date_of_birth: date

class ListAccountHolder:
    id: int
    username: str
    first_name: str
    last_name: str
    phone_number: str

class AccountHolderDetails:
    username: str
    first_name: str
    last_name: str
    email: str
    address: str
    phone_number: str
    date_of_birth: date

class EditAccountHolder:
    username: str
    first_name: str
    last_name: str
    email: str
    address: str
    phone_number: str
    date_of_birth: date
    date_updated: date