from flask import request

# Get HTTP request from website
import requests

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#@app.route('/login', methods=['POST', 'GET'])
#def login():
 #   error = None
  #  if request.method == 'POST':
   #     if valid_login(request.form['username'],
    #                   request.form['password']):
     #       return log_the_user_in(request.form['username'])
      #  else:
       #     error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    #return render_template('login.html', error=error)

#parameters taken from the library's API
#parameters = {
 #   "user_id": user,
  #  "b_title": title
#}

#url of the site, including user id and title/s.
# url with .json in the end
#API end point
#response = requests.get(url= , params=parameters)
#response.raise_for_status()

#response from the library website is stored here
#lib_books = response.json()

#formating the names of the new books to the recommender
#title = lib_books["title"]


