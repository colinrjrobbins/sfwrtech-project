from flask import Flask, render_template, request

app = Flask(__name__,
            static_folder='static',
            template_folder='templates')

listHold = []

@app.route('/')
def main():
    return render_template('index.html', title="CheaperPrice", signedIn="Not Signed In.")

@app.route('/searchProduct', methods=['POST'])
def searchProduct():
    # api call to check product information
    send_test_data = request.form['product']
    listHold.append(send_test_data)
    print(send_test_data)
    return render_template('index.html', title="CheaperPrice", searchItems=listHold, signedIn="Not Signed In.")

@app.route('/checkEmail', methods=['POST'])
def checkEmail():
    # database call to see if email exists
    email = request.form['email']
    print(email)
    return render_template('index.html', title="CheaperPrice", signedIn=email)

@app.route('/saveItem', methods=['POST'])
def saveItem():
    choice = request.form.get('value')
    print(choice)
    return render_template('index.html', title="CheaperPrice", searchItems=listHold, signedIn="Not Signed In.")


if __name__ == '__main__':
    app.run(debug=True)