from flask_restful import Resource
from flask import make_response, render_template


class HomePage(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'), 200, headers)


class UserHomePage(Resource):
    # Täytyy olla kirjautunut, että pääsee sivuun
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('user_home.html'), 200, headers)
