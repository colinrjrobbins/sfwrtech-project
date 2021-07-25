######################################################
# Program: MovieList
# Class: User
# Purpose: Keeps track of a universal movie list for
#          the user as well as the users email to be
#          called when required.
###################################################### 
class User:

    def __init__(self): 
        """Initializes the User class with an empty email and movie list to update after login."""
        self.email = None
        self.movie_list = []

    def update_email(self, email):
        """Takes in the newly added email and updates it from None to email."""
        self.email = email
    
    def restore_movie_list(self, movie_list):
        """Takes in the saved user list and updates the user movie list with that inforation."""
        self.movie_list = movie_list

    def view_movie_list(self):
        """Simply returns the users movie list as a list of lists."""
        return self.movie_list