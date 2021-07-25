#######################################################
# Program: MovieList
# Architecture: Attempted Facade Pattern
# Classes: Search (Facade Interface), IMDbCall, TMDbCall
# Purpose: Calls upon both the IMDb API and TMDb API 
#          classes to access and prepare based on the 
#          query string of the movie name given. 
#          returns a single dictonary of search results.
####################################################### 

import configparser
import json
import requests

import imdb

class Search:
    """Search class used to initialize the IMDbCall class and TMDbCall class.
    Returns the search results organized in a dictonary."""

    def __init__(self):
        """Creates the IMDBCall and TMDBCall objects as well an empty dictionary."""

        self.__imdbCall = IMDbCall()
        self.__tmdbCall = TMDbCall()
        self.__search_results = {}

    def search(self, query):
        """Takes in the movie name as a query string, makes the calls and returns
        the search results as an organized dictionary."""

        self.__imdbCall.call(query)
        self.__search_results['IMDb'] = self.__imdbCall.result_call()
        self.__tmdbCall.call(query)
        self.__search_results['TMDb'] = self.__tmdbCall.result_call()
        return self.__search_results

class IMDbCall:
    """Uses the Python IMDb wrapper to call and get the required movies.
    Note: These are unfiltered and will display adult content."""

    def __init__(self):
        """Create the initial IMDb instance and a blank result dictonary for 
        sorting all the results in an organized manor."""

        self.__imdbapi = imdb.IMDb()
        self.__results = {}
    
    def call(self,query):
        """Takes in the query, organizes the information and saves it to the class 
        results attribute."""

        self.__results.clear()

        movies = self.__imdbapi.search_movie(query)
        
        x = 0
        for movie in movies:
            hold_list = []
            id = movie.movieID
            selected_movie = self.__imdbapi.get_movie(id)
            hold_list.append(selected_movie.get('title') + ' ('+ str(selected_movie.get('year')) + ')')
            try:
                hold_list.append(selected_movie.get('plot')[0])
            except:
                hold_list.append("No Plot available.")
            self.__results[x] = hold_list
            x += 1

    def result_call(self):
        """Used to return the private result data."""

        return self.__results

class TMDbCall:
    """Makes a call to the movie database using the given API, and returns the data based on the query given."""

    def __init__(self):
        """Opens up the configuration file and gathers the API key for TMDb, also creates a blank result dictonary attribute."""

        self.__config = configparser.ConfigParser()
        self.__config.read('modules/config.cfg')
        self.__apiKey = self.__config['TMDb']['apiKey']
        self.__results = {}
    
    def call(self, query):
        """Runs a request to TMDb to get the title and overview of the given movie query."""

        self.__results.clear()

        query = query.replace(' ', '%20')
        request_data = requests.get('https://api.themoviedb.org/3/search/movie?api_key='+self.__apiKey+'&language=en-US&query='+query+'&page=1&include_adult=false')
        result_data = json.loads(request_data.text)

        x = 0
        for movie in result_data['results']:
            hold_list = []
            hold_list.append(movie['original_title'])
            hold_list.append(movie['overview'])
            self.__results[x] = hold_list
            x+=1                 
    
    def result_call(self):
        """Returns the private results dictonary for use in the main program."""
        return self.__results
