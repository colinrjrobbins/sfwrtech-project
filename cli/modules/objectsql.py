#######################################################
# Program: MovieList
# Architecture: ObjectPool
# Classes: Reusable, DatabasePool and UseDatabase
# Purpose: Configured as a Database Object Pool to grab
#          and use the connection as required and then
#          release the connection back to the pool
#          after the necessary calls have been made to 
#          the database.
####################################################### 

from mysql.connector import connect
import configparser
from datetime import datetime as dt

class Reusable:
    """Creates a reusable database connection. Not callable by the user."""

    def __init__(self):
        """Initializes the database connection to be stored in a pool list
        and reused as necessary."""
    
        config = configparser.ConfigParser()
        config.read('modules/config.cfg')

        self.conn = connect(
            host=config['Database']['host'],
            user=config['Database']['user'],
            password=config['Database']['password']
        )

        # Starts the connection by setting the main database for use so each additional
        # database connection will always have access without having to call it at the
        # start of each function.
        with self.conn.cursor() as cursor:
            cursor.execute("USE " + config['Database']['database'] + ';')

    def __del__(self):
        """Acts as a "garbage collector" so the connection is closed before the
        program ends."""

        self.conn.close()

class DatabasePool:
    """Creates a database pool to store the Reusable() instances, can acquire connections
    and release them back to the pool."""

    def __init__(self):
        """Initializes the Pool by creating a Reusable connection to the database."""

        self.__connections = [Reusable()]

    def acquire(self):
        """Allows the program to call and attach to the database so calls can be made."""

        return self.__connections.pop()

    def release(self, reusable):
        """Returns the connection back to the database pool."""

        self.__connections.append(reusable)

class UseDatabase:
    """Used by the client to call different SQL statements to the database, they are preconfigured for
    optimized queries and statements."""

    def __init__(self):
        """Initializes by creating a Database pool to gather reusable connections when required."""

        self.__getConnection = DatabasePool()

    def check_user(self, email):
        """Used to check the email given to see if it is already stored in the database and
        returns True or False based on if the user already has a movie list saved."""

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
        """Takes in an email and the blank User.movie_list to append the saved data from
        the database onto it."""

        self.db = self.__getConnection.acquire()
        query = "SELECT search_type, movie_name, movie_description FROM user_list WHERE email='"+email+"';"
        
        with self.db.conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            for row in result:
                movie_list.append([row[0],row[1],row[2]])
        
        self.__getConnection.release(self.db)

    def update_list(self, email, movie_list):
        """Acquires the database connection, drops the previous saved list for the user and updates it
        with the new list to be stored. This is called upon exiting the program."""

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
                    # movie_list is setup as ['IMDb/TMDb','Movie Name','Movie Description']
                    item[2] = item[2].replace("'","")
                    query = "INSERT INTO user_list(email, movie_name, movie_description, search_type, saved_date) VALUES('"+email+"','"+item[1]+"','"+item[2]+"','"+item[0]+"','"+format_date+"')"
                    cursor.execute(query)
                    self.db.conn.commit()
        
        self.__getConnection.release(self.db)

