from flask import Flask, render_template, request

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

listHold = []
savedList = []

@app.route('/')
def main():
    return render_template('index.html', 
                           title="CheaperPrice", 
                           signedIn="Not Signed In.")

@app.route('/searchProduct', methods=['POST'])
def searchProduct():
    # api call to check product information
    product_search = request.form['product']
    listHold.append({'id': None,
                     'name':product_search})
    print(product_search)
    print(listHold)
    for x in range(0,len(listHold)):
        listHold[x]['id'] = x

    print(listHold)
    return render_template('index.html',
                           title="CheaperPrice", 
                           searchItems=listHold, 
                           savedItems=savedList,
                           signedIn="Not Signed In.")

@app.route('/checkEmail', methods=['POST'])
def checkEmail():
    # database call to see if email exists
    email = request.form['email']
    print(email)
    return render_template('index.html', 
                           title="CheaperPrice", 
                           savedItems=savedList,
                           signedIn=email)

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