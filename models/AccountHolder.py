class AccountHolder:
    id: int
    first_name: str
    last_name: str
    email: str
    phone_number: str

    def __init__(self, email: str, first_name="", last_name="", phone_number=""):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.id}\t{self.first_name}\t{self.last_name}\t{self.email}\t{self.phone_number}"
