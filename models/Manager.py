class Manager:
    id: int
    first_name: str
    last_name: str
    email: str
    password: str
    phone_number: str

    def __init__(self, email: str, password: str, first_name="", last_name="", phone_number=""):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.id}\t{self.first_name}\t{self.last_name}\t{self.email}\t{self.password}\t{self.phone_number}"

