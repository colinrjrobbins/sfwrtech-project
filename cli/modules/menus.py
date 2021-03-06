#######################################################
# Program: MovieList
# Classes: Menu
# Purpose: Main interface for the program. Is used as a
#          visual menu display as well as a main access
#          to create required classes.
####################################################### 

# CUSTOM IMPORTS
from modules.objectsql import UseDatabase
from modules.apicalls import Search
from modules.user import User
from modules.sendsave import SendEmail, SaveFile
from modules.clearscreen import clear
class Menu:
    """Used to create and execute different visual menues for ease of access."""

    def __init__(self):
        """Upon instantiated creates the base User() class, the UseDatabase() class
        and the Search() class."""

        self.__user = User()
        self.__option = None
        self.__db = UseDatabase()
        self.__search = Search()

    def login_menu(self):
        """Simple menu used to gather the users email and check it with the database
        to determine whether the list should be recovered or not."""

        while self.__user.email == None or self.__user.email == '':
            print('Welcome to MovieList!' +\
                '\nPlease enter your email to continue.\n')
            email = input('Email ==> ')

            self.__user.update_email(email)
            
            if self.__user.email == None or self.__user.email == '':
                clear()
                print('\n!!! ---- Please enter an email. ---- !!!\n')
            else:
                check = self.__db.check_user(self.__user.email)
            
                if check == True:
                    while True:
                        print('\nThere is an old version of your list.')
                        print('Would you like to restore it?')
                        try:
                            option = str.upper(input("(Y or N) ==> "))
                            if option == "Y":
                                self.__db.restore_movie_list(self.__user.email, self.__user.movie_list)
                                clear()
                                print('List Restored.')
                                input('Press any key to continue to the program...')
                                clear()
                                break
                            elif option == 'N':
                                clear()
                                break
                            else:
                                clear()
                                print("Not an option...please try again.")
                        except:
                            pass
                else:
                    pass
        
    def main_menu(self):
        """Main interface to the majority of the program. Allows the user to decide what to do next,
        whether it is to search through and add movies, see your personal list, or send or save it."""

        while self.__option != 5:
            print('\nMovieList\n'+\
                'Created by Colin Robbins for SFWRTECH 4SA3\n'+\
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
                clear()
                self.search_menu()

            elif self.__option == 2:
                clear()
                self.personal_list_menu()
            
            elif self.__option == 3:
                self.__send_email = SendEmail(self.__user.email, self.__user.movie_list)
                self.__send_email.prepare_email()
                self.__send_email.send_email()
                clear()

            elif self.__option == 4:
                print("What should the save file be named?")
                filename = input("Save File Name ==> ")
                filename = filename+'.txt'
                self.__save_file = SaveFile(self.__user.email, self.__user.movie_list)
                self.__save_file.prepare_save_file()
                self.__save_file.save_file(filename)
                print("File has been saved in the saveFiles folder.")
                input('Press any key to return to menu...')
                clear()

            elif self.__option == 5:
                print('Saving to Database...')
                self.__db.update_list(self.__user.email, self.__user.movie_list)
                input('Press any key to exit the program, save is complete.')
                exit()

            else:
                clear()
                print("Not an option. Try again.")

    def search_menu(self):
        """Menu used to call the Search class and supply it with a query. Then print out the
        results for both IMDb and TMDb."""

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
                print("Search takes roughly 30 seconds to complete...")
                results = self.__search.search(movieString)
                while True:
                    clear()
                    print(header+\
                          '(1)\tIMDb (Internet Media Database) Results\n'+\
                          '(2)\tTMDb (The Movie Database) Results\n'+\
                          '(3)\tReturn to Search Menu\n\n')
                    try:
                        choice = int(input('Option ==> '))
                        if choice == 1:
                            clear()
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
                            clear()
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
                            clear()
                            break
                        else:
                            clear()
                            print('Not an option try again.')
                            input('Press any key to continue...')
                    except KeyboardInterrupt:
                        clear()
                        break
            except KeyboardInterrupt:
                clear()
                break
            except:
                clear()
                print('Not an option try again.')
                input('Press any key to continue...')

    def personal_list_menu(self):
        """Used to view the list and remove entries if no longer required."""

        while True:
            print('This is the movie list for: ' + self.__user.email + '\n' +\
                  '\t\tPersonal Movie List\n' +\
                  '*********************************************\n\n')
            
            personal_list = self.__user.view_movie_list()
            
            # If personal list is empty, return no results.
            if personal_list == []:
                print('No movies currently added to list.')
                input('Press any key to return to the menu...')
                break
            # else print for the each list by api check type.
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
                        clear()
                        print('\nItem has been removed.\n')
                    except KeyboardInterrupt:
                        clear()
                        break
                    except:
                        clear()
                        print("Not a valid option. Try again.")
                except:
                    clear()
                    print('No movies currently in list.')
                    input('Press any key to return to the menu...')
                    break