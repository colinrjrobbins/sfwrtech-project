#######################################################
# Program: MovieList
# Classes: SendEmail and SaveFile
# Purpose: Used to configure and prepare the movie list
#          to send to the given email or to save to a
#          file for viewing later. 
####################################################### 

import configparser
import smtplib

class SendEmail:
    """Used to send the movie list in an organized fashion to the given email."""

    def __init__(self, email, movie_list):
        """Takes in email and movie list and prepares all the required
        information as protected variables for use in sending the email."""

        self.email = email
        self.movie_list = movie_list
        self.__subject = "Subject: Movie List Result\n\n"
        self.__config = configparser.ConfigParser()
        self.__config.read('modules/config.cfg')
        self.__host = self.__config['Email']['host']
        self.__port = self.__config['Email']['port']
        self.__sender_email = self.__config['Email']['email']
        self.__password = self.__config['Email']['password']
        self.__message = ""

    def prepare_email(self):
        """Prepares the email in an organized format to send to the given email,
        returns nothing."""

        self.__message = "IMDb\n------------------------\n"
        for movie in self.movie_list:
            if movie[0] == 'IMDb':
                self.__message += "Title: " + movie[1] +"\n"
                self.__message += "Overview: " + movie[2] + "\n\n"
        self.__message += "TMDb\n------------------------\n"
        for movie in self.movie_list:
            if movie[0] == 'TMDb':
                self.__message += "Title: " + movie[1] + "\n"
                self.__message += "Overview: " + movie[2] + "\n\n"
 
    def send_email(self):
        """Takes the prepared email message from the class attributes and creates an smtp 
        server to send the email to the users email."""
        
        try:
            server = smtplib.SMTP_SSL(self.__host, self.__port)
            server.ehlo()
            server.login(self.__sender_email, self.__password)
            server.sendmail(self.__sender_email, self.email, self.__subject+self.__message)
            server.close()
            print("Email sent.")
            input('Press any key to return to menu...')
        except:
            print("Couldn't send email.'")
            input("Press any key to return to menu...")

class SaveFile:
    """Used to save the movie list as a TXT file for viewing later."""

    def __init__(self, email, movie_list):
        """Takes the prepared email and movie list and prepares the
        required data from the saved configuration file."""
        
        self.email = email
        self.movie_list = movie_list
        self.__config = configparser.ConfigParser()
        self.__config.read('modules/config.cfg')
        self.__message = ""
    
    def prepare_save_file(self):
        """Prepare the movie list in a clean text file to be saved 
        post execution."""

        self.__message = "IMDb\n------------------------\n"
        for movie in self.movie_list:
            if movie[0] == 'IMDb':
                self.__message += "Title: " + movie[1] +"\n"
                self.__message += "Overview: " + movie[2] + "\n\n"
        self.__message += "TMDb\n------------------------\n"
        for movie in self.movie_list:
            if movie[0] == 'TMDb':
                self.__message += "Title: " + movie[1] + "\n"
                self.__message += "Overview: " + movie[2] + "\n\n"

    def save_file(self, filename):
        """Takes in the requested filename and saves it into the saveFiles
        folder."""
        
        file = open('saveFiles/'+filename,'w+')
        file.write(self.__message)
        file.close()