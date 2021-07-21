class Menu:
    def __init__(self):
        self.__email = None
        self.__option = None

    def login_menu(self):
        while self.__email == None or self.__email == '':
            print('Welcome to MovieList!' +\
                '\nPlease enter your email to continue.\n')
            self.__email = input('Email ==> ')
            if self.__email == None or self.__email == '':
                print('\n!!! ---- Please enter an email. ---- !!!\n')
            else:
                pass
        
    def main_menu(self):
        while self.__option != 5:
            print('\nMovieList\n'+\
                'Created by Colin Robbins for SFWRTECH\n'+\
                'Welcome user: ' + self.__email + '\n' +\
                '\t\tMAIN MENU\n'+\
                '*********************************************\n\n'+\
                '(1)\tSearch for Movie to Add\n'+\
                '(2)\tSee movies in Personal Saved List\n'+\
                '(3)\tSend Personal List as Email\n'+\
                '(4)\tSave Personal List as File\n' +\
                '(5)\tExit\n')
            self.__option = int(input('Option ==> '))

            if self.__option == 1:
                pass
            elif self.__option == 2:
                pass
            elif self.__option == 3:
                pass
            elif self.__option == 4:
                pass
            elif self.__option == 5:
                exit()

    def search_menu(self):
        
