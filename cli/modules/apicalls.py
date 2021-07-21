import configparser
import json
import requests

import imdb

class Search:
    def __init__(self, search_item):
        pass

    

imdbSearch = imdb.IMDb()

movies = imdbSearch.search_movie('The Matrix')
id = movies[0].movieID
print(id)

# config = configparser.ConfigParser()
# config.read('config.cfg')

# apikey = config['TMDb']['apiKey']

# request_data = requests.get('https://api.themoviedb.org/3/search/movie?api_key=74d83304b31ec0a74ef68fc6159ad5eb&language=en-US&query=The%20Matrix&page=1&include_adult=false')
# result_data = json.loads(request_data.text)

# title = []
# overview = []

# for x in range(0, len(result_data['results'])):
#     for movie in result_data['results']:
#         # print(movie)
#         title.append(movie['original_title'])
#         overview.append(movie['overview'])

# for x in range(0, 3):
#     print("("+str(x+1)+")" + " : " + title[x] + " : " + overview[x] + "\n" )

