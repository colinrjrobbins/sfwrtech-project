from flask import Flask, render_template, request

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

listHold = []
savedList = []
ITERATE = 0

@app.route('/')
def main():
    return render_template('index.html', 
                           title="CheaperPrice", 
                           signedIn="Not Signed In.")

@app.route('/searchProduct', methods=['POST'])
def searchProduct():
    # api call to check product information
    product_search = request.form['product']
    listHold.append({'id':ITERATE+1,
                     'name':product_search})
    
    print(product_search)
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

@app.route('/saveItem', methods=['POST'])
def saveItem():
    choice = request.form['name']
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