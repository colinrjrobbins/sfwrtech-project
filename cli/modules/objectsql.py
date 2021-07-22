from mysql.connector import connect
import configparser
from datetime import datetime as dt

class Reusable:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('modules/config.cfg')

        self.conn = connect(
            host=config['Database']['host'],
            user=config['Database']['user'],
            password=config['Database']['password']
        )
        with self.conn.cursor() as cursor:
            cursor.execute("USE " + config['Database']['database'] + ';')

    def __del__(self):
        self.conn.close()

class DatabasePool:
    def __init__(self):
        self.__connections = [Reusable()]

    def acquire(self):
        return self.__connections.pop()

    def release(self, reusable):
        self.__connections.append(reusable)

class UseDatabase:
    def __init__(self):
        self.__getConnection = DatabasePool()

    def check_user(self, email):
        self.db = self.__getConnection.acquire()
        query = "SELECT * FROM user_list WHERE (email = '" + email +"');"
        with self.db.conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            if result == []:
                self.__getConnection.release(self.db)
                return False
            else:
                self.__getConnection.release(self.db)
                return True
        
    def restore_movie_list(self, email, movie_list):
        self.db = self.__getConnection.acquire()
        query = "SELECT search_type, movie_name, movie_description FROM user_list WHERE email='"+email+"';"
        with self.db.conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                movie_list.append([row[0],row[1],row[2]])
        self.__getConnection.release(self.db)

    def update_list(self, email, movie_list):
        now = dt.now()
        format_date = str(now.strftime('%Y-%m-%d'))
        self.db = self.__getConnection.acquire()
        if movie_list == []:
            pass
        else:
            with self.db.conn.cursor() as cursor:
                query="DELETE FROM user_list WHERE email='"+email+"';"
                cursor.execute(query)
                self.db.conn.commit()
                for item in movie_list:
                    # assume movie_list is setup as ['IMDb/TMDb','Movie Name','Movie Description']
                    query = "INSERT INTO user_list(email, movie_name, movie_description, search_type, saved_date) VALUES('"+email+"','"+item[1]+"','"+item[2]+"','"+item[0]+"','"+format_date+"')"
                    cursor.execute(query)
                    self.db.conn.commit()
        self.__getConnection.release(self.db)

