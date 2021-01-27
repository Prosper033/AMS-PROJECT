from models.Manager import Manager


class ManagersManager:

    managers = []

    def create_manager(self, first_name: str, middle_name: str, last_name: str, email: str, password: str):
        manager_id = self.__get_id
        manager = Manager(id=manager_id, last_name=last_name,
                          email=email, password=password)
        return True

    def update_manager(self, first_name: str, middle_name: str, last_name: str, email):
        manager = self.__find(email)
        if manager != None:
            manager

    def __get_id(self):
        length = len(self.managers)
        if length == 0:
            length += 1
            return length
        else:
            for manager in self.managers:
                if manager.id == length:
                    length += 1
                    return length

    def __find(email):
        for manager in self.managers:
            if manager.email == email:
                return manager
            else:
                return None
