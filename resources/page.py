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


class MovieList(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('movie_lists.html'), 200, headers)


# Authentication

class LoginPage(Resource):
    def get(self):

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('login.html'), 200, headers)


class RegisterPage(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('register.html'), 200, headers)


# Tuleeko nää tähän vai pitääkö tehdä oma resources/movie_list.py ?
class CreateList(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('create_list.html'), 200, headers)


class EditList(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('edit_list.html'), 200, headers)


class ViewList(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('view_list.html'), 200, headers)
