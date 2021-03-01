from typing import List

from repositories.BaseRepository import BaseRepository
from models.Manager import Manager


class ManagerRepository(BaseRepository):
    def __init__(self):
        super().__init__()
        self.db = BaseRepository.db

    def create(self, manager: Manager):
        cursor = self.db.cursor()
        sql = "INSERT INTO manager (first_name, last_name, email, password, phone_number) values (%s, %s, %s, %s, %s)"
        val = (manager.first_name, manager.last_name, manager.email,
               manager.password, manager.phone_number)
        cursor.execute(sql, val)
        self.db.commit()
        manager.id = cursor.lastrowid

    def find(self, email: str):
        cursor = self.db.cursor()
        sql = "SELECT first_name, last_name, email, password, phone_number FROM manager WHERE email = %s"
        val = (email,)
        cursor.execute(sql, val)
        record = cursor.fetchone()
        manager = ManagerRepository.__map_selected_record_to_manager(record)
        return manager

    def update(self, manager: Manager):
        cursor = self.db.cursor()
        sql = "UPDATE manager SET first_name = %s, last_name = %s, phone_number = %s, WHERE email = %s"
        val = (manager.first_name, manager.last_name, manager.phone_number)
        cursor.execute(sql, val)
        self.db.commit()

    def list(self):
        cursor = self.db.cursor()
        sql = "SELECT first_name, last_name, email, middle_name, phone_number, password FROM manager"
        cursor.execute(sql, )
        results = cursor.fetchall()
        managers: List[Manager] = []
        for record in results:
            manager = ManagerRepository.__map_selected_record_to_manager(record)
            managers.append(manager)
        return managers

    def delete(self, email: str):
        cursor = self.db.cursor()
        sql = "DELETE FROM manager WHERE email=%s"
        val = (email,)
        cursor.execute(sql, val)
        self.db.commit()

    def change_password(self, email: str, new_password: str):
        cursor = self.db.cursor()
        sql = "UPDATE manager SET password = %s WHERE email = %s"
        val = (new_password, email)
        cursor.execute(sql, val)
        self.db.commit()

    @staticmethod
    def __map_selected_record_to_manager(record):
        if record is None:
            return None
        first_name, last_name, email, password, phone_number = record
        account_holder = Manager(email=email, password=password, first_name=first_name, last_name=last_name,
                                       phone_number=phone_number)
        account_holder.id = id
        return account_holder
