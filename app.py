from flask import Flask # import Flask in Python

app = Flask(__name__) # creates an instance of a Flask app
@app.route('/') # route called by user
def index(): # function called by '/' route
    return 'Hello World! This App is built using Flask. version=1'
app.run(host='0.0.0.0', port=8000) # starts the web app at port 8000

@app.route('/api/prediction', methods=['POST'])
def prediction():
    return 'Hello, this page is to test out POST method.'