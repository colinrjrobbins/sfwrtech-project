from flask import Flask, render_template, request
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

# Best Buy API key 
# WmGHeZFA7xhUZ3roKA891YhK 

# walmart requires a private key for connection 

# will need to substitute something else for costco, its a paid program

@app.route('/', methods=['GET', 'POST'])
def main():
    movieSearchForm = MovieSearch()
    emailForm = SignIn()

    if movieSearchForm.validate_on_submit():
        print('MovieName: {}\nGenre: {}\nYear: {}\n'.format(movieSearchForm.movieName.data, movieSearchForm.genre.data, movieSearchForm.year.data))

    if emailForm.validate_on_submit():
        print('Email: {}'.format(emailForm.email.data))

    return render_template('index.html', 
                           title="MovieList",
                           form=movieSearchForm,
                           email_form = emailForm,
                           signedIn="Not Signed In.")

# @app.route('/searchProduct', methods=['POST'])
# def searchProduct():
#     # api call to check product information
    
#     product_search = request.form['product']
#     listHold.append({'id': None,
#                      'name':product_search})
#     print(product_search)
#     print(listHold)
#     for x in range(0,len(listHold)):
#         listHold[x]['id'] = x

#     print(listHold)
#     return render_template('index.html',
#                            title="CheaperPrice", 
#                            searchItems=listHold, 
#                            savedItems=savedList,
#                            signedIn="Not Signed In.")

# @app.route('/checkEmail', methods=['POST'])
# def checkEmail():
#     # database call to see if email exists
#     email = request.form['email']
#     print(email)
#     return render_template('index.html', 
#                            title="CheaperPrice", 
#                            savedItems=savedList,
#                            signedIn=email)

# @app.route('/saveItem', methods=['GET','POST'])
# def saveItem():
#     try:
#         choice = request.form.get['0']
#         print(choice)
#     except:
#         print("No Gather")
                
#     choice = request.get_data()
#     savedData = request.data
#     savedList.append(choice)
#     print(choice)
#     print(savedData)
#     return render_template('index.html', 
#                             title="CheaperPrice", 
#                             searchItems=listHold, 
#                             savedItems=savedList,
#                             signedIn="Not Signed In.")

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