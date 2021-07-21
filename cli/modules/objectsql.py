import mysql.connector
import configparser

class Reusable:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.cfg')

        self.__conn = mysql.connector.connect(
            host=config['Database']['host'],
            user=config['Database']['user'],
            password=config['Database']['password']
        )

    def __del__(self):
        self.__conn.close()

class DatabasePool:
    def __init__(self):
        self.__connections = [Reusable()]

    def acquire(self):
        return self.__connections.pop()

    def release(self, reusable):
        self.__connections.append(reusable)
