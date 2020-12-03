from flask import Flask
from flask_restful import Api

from config import Config
from resources.page import HomePage, UserHomePage, MovieList, LoginPage, RegisterPage
import resources
import extensions


def create_app():

    app = Flask(__name__, static_url_path='/static')
    app.config.from_object(Config)

    # Defines all the extensions that the application uses (extensions/__init__.py)
    extensions.init_app(app)

    # Defines all the flask Resources we're using on the app (resources/__init__.py)
    resources.init_app(app)

    return app


def register_resources(app):
    api = Api(app)

    api.add_resource(HomePage, '/')
    api.add_resource(MovieList, '/movie-lists/')
    api.add_resource(UserHomePage, '/users/home')

    # Tämä tulee käyttöön, kun meillä on usersit tehty:
    # api.add_resource(UserHomePage, '/users/<string:username>/home')

    # Luodaan uusi lista
    # api.add_resource(#, '/users/<string:username>/create')

    # Editoidaan tietty lista
    # api.add_resource(#, '/users/<string:username>/<int:list_id>/edit')

    # Poistetaan tietty lista
    # api.add_resource(#, '/users/<string:username>/<int:list_id>/delete')

    api.add_resource(LoginPage, '/login')
    api.add_resource(RegisterPage, '/register')


if __name__ == "__main__":
    app = create_app()
    app.run()
