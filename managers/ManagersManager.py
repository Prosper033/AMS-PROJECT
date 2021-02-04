from models.Manager import Manager


class ManagersManager:

    manager: Manager

    def create_manager(self, first_name: str, last_name: str, phone_number: str, email: str, password: str):
        self.manager = Manager(last_name=last_name, email=email, password=password)
        self.manager.first_name = first_name
        self.manager.phone_number = phone_number
        return True

    def login(self, email, password):
        if self.manager.email == email and self.manager.password == password:
            return True
        else:
            return False

    def update_manager(self, first_name: str, last_name: str, phone_number: str):
        if self.manager is not None:
            self.manager.first_name = first_name
            self.manager.last_name = last_name
            self.manager.phone_number = phone_number
            return True
        else:
            return False

    def change_password(self, new_password: str):
        self.manager.password = new_password
        return True

    def view_details(self):
        print(self.manager.id, '\t', self.manager.first_name, '\t', self.manager.last_name,
              '\t', self.manager.email, '\t', self.manager.phone_number)


