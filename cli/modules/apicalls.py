import configparser
import json
import requests

import imdb

class Search:
    def __init__(self):
        self.__imdbCall = IMDbCall()
        self.__tmdbCall = TMDbCall()
        self.__search_results = {}

    def search(self, query):
        self.__imdbCall.call(query)
        self.__search_results['IMDb'] = self.__imdbCall.result_call()
        self.__tmdbCall.call(query)
        self.__search_results['TMDb'] = self.__tmdbCall.result_call()
        return self.__search_results

class IMDbCall:
    def __init__(self):
        self.__imdbapi = imdb.IMDb()
        self.__results = {}
    
    def call(self,query):
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
        return self.__results

class TMDbCall:
    def __init__(self):
        self.__config = configparser.ConfigParser()
        self.__config.read('modules/config.cfg')
        self.__apiKey = self.__config['TMDb']['apiKey']
        self.__results = {}
    
    def call(self, query):
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
        return self.__results


# search = Search()
# results = search.search('The Matrix')
# print('IMDb Results')
# for x in range(0,3):
#     print('\n('+str(x)+')\t Title:' + results['IMDb'][x][0])
#     print('\t Overview: ' + results['IMDb'][x][1])
# print('\n\n')
# print('TMDb Results')
# for x in range(0,3):
#     print('\n('+str(x)+')\t Title:' + results['TMDb'][x][0])
#     print('\t Overview: ' + results['TMDb'][x][1])