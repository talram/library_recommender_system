import flask
from flask_cors import CORS, cross_origin
from flask import request
import json
from recommend_system import recommend_book

# Create the app
app = flask.Flask(__name__)
CORS(app)


# A route to return all of the recommended books to the shelf.
@app.route('/recommender', methods=['POST'])
@cross_origin()
def get_books():
    print("Hello")
    request_params = request.json
    print(request_params)
    result = recommend_book(request_params['name'])

    response = {
        'user_id': request_params['user_id'],
        'isbns': result
    }
    return json.dumps(response)


if __name__ == '__main__':
    app.run()
