import configparser
import smtplib

class SendEmail:
    def __init__(self, email, movie_list):
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
        try:
            server = smtplib.SMTP_SSL(self.__host, self.__port)
            server.ehlo()
            server.login(self.__sender_email, self.__password)
            server.sendmail(self.__sender_email, self.email, self.__subject+self.__message)
            server.close()
            print("Email sent.")
        except:
            print("Couldn't send email.'")
            input("Press any key to return to menu...")

class SaveFile:
    def __init__(self, email, movie_list):
        self.email = email
        self.movie_list = movie_list
        self.__config = configparser.ConfigParser()
        self.__config.read('modules/config.cfg')
        self.__message = ""
    
    def prepare_save_file(self):
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
        file = open('saveFiles/'+filename,'w+')
        file.write(self.__message)
        file.close()