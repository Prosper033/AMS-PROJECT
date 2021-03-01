class Account:

    id: int
    account_holder_id: int
    account_name: str
    account_number: str
    pin: int
    balance: float
    status: str

    def __init__(self, account_number: str, pin: int, account_holder_id=0, account_name="",
                 balance=0.0, status=""):
        self.account_holder_id = account_holder_id
        self.account_number = account_number
        self.pin = pin
        self.account_name = account_name
        self.balance = balance
        self.status = status

    def __str__(self):
        return f"{self.id}\t{self.account_name}\t{self.account_number}\t{self.pin}\t{self.balance}\t{self.status}"
