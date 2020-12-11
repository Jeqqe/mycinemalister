from flask_restful import Api

from resources.auth import Login, Logout, Register
# from resources.user import UserListResource, UserResource, MeResource <- Ei käytössä tällä hetkel
from resources.page import HomePage, UserHomePage
from resources.movie import EditList, ViewList, MovieList, SearchMovie, CreateMovieReview, EditMovieReview


# Each resource created under resources/ that we want to use should be added here,
# create_app() will then call the init_app() function on app.py to set them up.
# This makes the app file look much cleaner & more organized.


def init_app(app):

    api = Api(app)

    """
    # User resources
    api.add_resource(UserListResource, "/users")
    api.add_resource(UserResource, "/users/<string:username>")
    api.add_resource(MeResource, "/me")
    """

    # Auth resources
    api.add_resource(Login, "/auth/login")
    api.add_resource(Logout, "/auth/logout")
    api.add_resource(Register, "/auth/register")

    # Page resources
    api.add_resource(HomePage, "/")

    # Movie/review resources
    api.add_resource(SearchMovie, "/reviews/create")  # Uusien leffojen etsiminen ja luominen
    api.add_resource(MovieList, "/reviews/all")  # Kaikki reviewt näkyy tästä
    api.add_resource(ViewList, "/reviews/mine")  # Käyttäjän oma lista
    api.add_resource(EditList, "/reviews/<string:list_id>/edit") # Editoi tietyn listan
    api.add_resource(CreateMovieReview, "/reviews/new/<string:movie_id>")
    api.add_resource(EditMovieReview, "/reviews/edit/<string:review_id>")
