from flask import Flask, render_template, request, redirect, flash
from modules.forms import *
from modules.apiCalls import *
from modules.emailList import *
from modules.fileSave import *

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')
app.config['SECRET_KEY'] = 'dbnwuaigbdklegf3o284y9801yhwdqbd8iog7w8iogka'

listHold = []
savedList = []

# def checkEmail(emailForm):
#     # database call to see if email exists
#     email = emailForm.email.data
    
#     database = ['colinrjrobbins@gmail.com']

#     # run database check on email
#     if email in database:
#         return True
#     else:
#         return False


@app.route('/', methods=['GET','POST'])
def login():
    emailForm = SignIn()
    searchList = SearchResult()

    if emailForm.validate_on_submit():
        return main(emailForm, searchList)

    searchList = None
    emailForm.email.data = None
    return render_template('login.html', form=emailForm)


@app.route('/main', methods=['GET', 'POST'])
def main(emailForm, searchList):
    print(emailForm.email.data)
    if emailForm.email.data == None:
        return redirect('/')

    movieSearchForm = MovieSearch()

    if movieSearchForm.validate_on_submit():
        return searchMovie(movieSearchForm, emailForm)

    # result = checkEmail(emailForm)
    # if result == True:
    #     print('Email previously used.')
    # else:
    #     print('Email not previously used.')

    return render_template('index.html', 
                           title="MovieList",
                           form=movieSearchForm,
                           searchItems=searchList,
                           signedIn=emailForm.email.data)

@app.route('/searchMovie', methods=['GET','POST'])
def searchMovie(movieSearchForm, emailForm):
    # api call to check movie information
    
    movie_name = movieSearchForm.movieName.data
    listHold.append({'id': None,
                     'name':movie_name})
    print(movie_name)
    for x in range(0,len(listHold)):
        listHold[x]['id'] = x

    print(listHold)
    return main(emailForm)

    
@app.route('/saveItem', methods=['GET','POST'])
def saveItem():
    try:
        choice = request.form.get['0']
        print(choice)
    except:
        print("No Gather")
                
    choice = request.get_data()
    savedData = request.data
    savedList.append(choice)
    print(choice)
    print(savedData)
    return render_template('index.html', 
                            title="CheaperPrice", 
                            searchItems=listHold, 
                            savedItems=savedList,
                            signedIn="Not Signed In.")

@app.route('/saveList', methods=['POST'])
def saveList():
    pass
    # save to both database and file here

@app.route('/sendAsEmail', methods=['POST'])
def sendAsEmail():
    pass
    # send a sorted list as an email here

if __name__ == '__main__':
    app.run(debug=True)