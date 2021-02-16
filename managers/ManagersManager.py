from models.Manager import Manager

class ManagersManager:
    manager_list = []

    file = open("Manager.txt", "a+")

    def create_manager(self, email: str, password: str, confirm_password: str, first_name: str, middle_name, last_name, phone):
        themanager = Manager(email=email, first_name=first_name, password=password)
        themanager.middle_name = middle_name
        themanager.last_name = last_name
        themanager.phone = phone
        self.manager_list.append(themanager)
        if self.file.closed is True:
            self.file = open("Manager.txt", "a+")
        else:
            self.file.write(f"{str(themanager)}""\n")
            self.file.flush()
        return True
    
    def update_manager(self, email: str, first_name: str, last_name: str, password: str, middle_name: str, phone: str):
        manager = self.__find(email)
        if manager is not None:
            manager.first_name = first_name
            manager.last_name = last_name
            manager.middle_name = middle_name
            manager.phone = phone
            self.__refresh_file()
            return True
        else:
            return False
        
    def show_manager(self):
        for manager in self.manager_list:
            self.__show(manager)

    def login(self, email: str, password: str):
        for manager in self.manager_list:
            if manager.email == email and manager.password == password:
                return manager
            else:
                return False

    def change_password(self, email: str, password: str, new_password: str):
        manager = self.__find(email)
        if manager:
            if manager.password == password:
                manager.password = new_password
                self.__refresh_file()
                return True
            else:
                return False
        else:
            return False

    def __find(self, email: str):
        for manager in self.manager_list:
            if manager.email == email:
                return manager
            else:
                return None

    def __show(self, manager: Manager):
        print('MANAGER NAME: ' + manager.first_name + ' ' + manager.middle_name + ' ' + manager.last_name, '\n' 'MANAGER EMAIL ' + manager.email, '\n' 'MANAGER PHONE NUMBER: ' + manager.phone )

    def __refresh_file(self):
        self.file = open("Manager.txt", "w")
        for manager in self.manager_list:
            self.file.write(str(manager))
            self.file.write("\n")
        self.file.flush()
