from modules.objectsql import UseDatabase
from modules.apicalls import Search
from modules.user import User
from modules.sendsave import SendEmail, SaveFile
class Menu:
    def __init__(self):
        self.__user = User()
        self.__option = None
        self.__db = UseDatabase()
        self.__search = Search()

    def login_menu(self):
        while self.__user.email == None or self.__user.email == '':
            print('Welcome to MovieList!' +\
                '\nPlease enter your email to continue.\n')
            email = input('Email ==> ')
            self.__user.update_email(email)
            if self.__user.email == None or self.__user.email == '':
                print('\n!!! ---- Please enter an email. ---- !!!\n')
            else:
                check = self.__db.check_user(self.__user.email)
                if check == True:
                    while True:
                        print('There is an old version of your list.')
                        print('Would you like to restore it?')
                        try:
                            option = str.upper(input("(Y or N) ==> "))
                            if option == "Y":
                                self.__db.restore_movie_list(self.__user.email, self.__user.movie_list)
                                print('List Restored.')
                                input('Press any key to continue to the program...')
                                break
                            elif option == 'N':
                                break
                            else:
                                print("Not an option...please try again.")
                        except:
                            pass
                    # take to restore menu items
                else:
                    pass
        
    def main_menu(self):
        while self.__option != 5:
            print('\nMovieList\n'+\
                'Created by Colin Robbins for SFWRTECH\n'+\
                'Welcome user: ' + self.__user.email + '\n' +\
                '\t\tMAIN MENU\n'+\
                '*********************************************\n\n'+\
                '(1)\tSearch for Movie to Add\n'+\
                '(2)\tSee movies in Personal Saved List\n'+\
                '(3)\tSend Personal List as Email\n'+\
                '(4)\tSave Personal List as File\n' +\
                '(5)\tExit\n')
            self.__option = int(input('Option ==> '))

            if self.__option == 1:
                self.search_menu()
            elif self.__option == 2:
                self.personal_list_menu()
            elif self.__option == 3:
                self.__send_email = SendEmail(self.__user.email, self.__user.movie_list)
                self.__send_email.prepare_email()
                self.__send_email.send_email()
            elif self.__option == 4:
                print("What should the save file be named?")
                filename = input("Save File Name ==> ")
                filename = filename+'.txt'
                self.__save_file = SaveFile(self.__user.email, self.__user.movie_list)
                self.__save_file.prepare_save_file()
                self.__save_file.save_file(filename)
                print("File has been saved in the saveFiles folder.")
            elif self.__option == 5:
                print('Saving to Database...')
                self.__db.update_list(self.__user.email, self.__user.movie_list)
                input('Press any key to exit the program, save is complete.')
                exit()

    def search_menu(self):
        while True:
            header = '\nSearch Menu\n' +\
                     '\n' +\
                     '*********************************************\n'
            print(header+\
                  'Please enter a movie title, it will search through\n'+\
                  'IMDb and TMDb for results. Use Control + C to return\n' +\
                  'to the main menu.\n'+\
                  '(CTRL+C)\tReturn to Menu\n')
            try:
                movieString = input('Movie Name ==> ')
                results = self.__search.search(movieString)
                while True:
                    print(header+\
                          '(1)\tIMDb (Internet Media Database) Results\n'+\
                          '(2)\tTMDb (The Movie Database) Results\n'+\
                          '(3)\tReturn to Search Menu\n\n')
                    try:
                        choice = int(input('Option ==> '))
                        if choice == 1:
                            print(header+\
                                  'IMDb Results\n\n')
                            for x in range(0,3):
                                print('\n('+str(x)+')\t Title: ' + results['IMDb'][x][0])
                                print('\t Overview: ' + results['IMDb'][x][1])
                            print('\n If you would like to chose one of these movies to add\nto your personal list, type the number.\n')
                            print('(4)\t Return to Previous menu.')
                            movie_choice = int(input('Option ==> '))
                            if movie_choice == 4:
                                pass
                            else:
                                self.__user.movie_list.append(['IMDb',results['IMDb'][movie_choice][0],results['IMDb'][movie_choice][1]])
                        elif choice == 2:
                            print(header+\
                                  'TMDb Results\n\n')
                            for x in range(0,3):
                                print('\n('+str(x)+')\t Title: ' + results['TMDb'][x][0])
                                print('\t Overview: ' + results['TMDb'][x][1])
                            print('\n If you would like to chose one of these movies to add\nto your personal list, type the number.\n')
                            print('(4)\t Return to Previous menu.')
                            movie_choice = int(input('Option ==> '))
                            if movie_choice == 4:
                                pass
                            else:
                                self.__user.movie_list.append(['TMDb',results['TMDb'][movie_choice][0],results['TMDb'][movie_choice][1]])
                        elif choice == 3:
                            break
                        else:
                            print('Not an option try again.')
                    except KeyboardInterrupt:
                        break
            except KeyboardInterrupt:
                break
            except:
                print('Not an option. Try again.')

    def personal_list_menu(self):
        while True:
            print('This is the movie list for: ' + self.__user.email + '\n' +\
                  '\t\tPersonal Movie List\n' +\
                  '*********************************************\n\n')
            personal_list = self.__user.view_movie_list()
            if personal_list == []:
                print('No movies currently added to list.')
                input('Press any key to return to the menu...')
                break
            else:
                try:
                    print('IMDb')
                    print('----------------\n')
                    x = 0
                    for item in personal_list:
                        if item[0] == 'IMDb':
                            print('('+str(x)+')\tTitle: ' + item[1])
                            print('\t Overview: ' + item[2] + '\n')
                            x+=1
                        else:
                            pass
                    print('TMDb')
                    print('----------------\n')
                    for item in personal_list:
                        if item[0] == 'TMDb':
                            print('('+str(x)+')\tTitle: ' + item[1])
                            print('\t Overview: ' + item[2] + '\n')
                            x+=1
                        else:
                            pass
                    print('\nOptions\n*********************************************\n')
                    print('(#)\tRemove item from your list.')
                    print('(CTRL+C)\tReturn to Main Menu.\n')
                    try:
                        choice = int(input('Option ==> '))
                        del self.__user.movie_list[choice]
                        print('\nItem has been removed.\n')
                    except KeyboardInterrupt:
                        break
                except:
                    print('No movies currently in list.')
                    input('Press any key to return to the menu...')
                    break