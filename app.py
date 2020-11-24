from flask import Flask, request, render_template, make_response
from flask_restful import Resource, Api
from config import Config

import resources
import extensions

app = Flask(__name__)
api = Api(app)


class HomePage(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'), 200, headers)


class LoginPage(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('login.html'), 200, headers)

# Tuleeko nää classit resources kansioon?
# vittu ku flask on vammanen, django on miljoonaa kertaa parempi


api.add_resource(HomePage, '/')
api.add_resource(LoginPage, '/login/')

if __name__ == "__main__":
    app.run(debug=True)

    # print(Movie().searchMovie("Shrek")) lmao shrek
