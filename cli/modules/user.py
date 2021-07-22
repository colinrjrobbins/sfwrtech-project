class User:
    def __init__(self):
        self.email = None
        self.movie_list = []

    def update_email(self, email):
        self.email = email
    
    def restore_movie_list(self, movie_list):
        self.movie_list = movie_list

    def view_movie_list(self):
        return self.movie_list