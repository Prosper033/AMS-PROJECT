import mysql.connector


class BaseRepository:
    db = None

    def __init__(self):
        if self.db is None:
            BaseRepository.db = mysql.connector.connect(host="localhost",
                                                        user="root",
                                                        password="Prosperous033",
                                                        database="ams")
