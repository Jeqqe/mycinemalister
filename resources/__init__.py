from flask_restful import Api

from resources.auth import LoginResource, LogoutResource, RegisterResource
from resources.user import UserListResource, UserResource, MeResource
from resources.page import HomePage, LoginPage, RegisterPage, MovieList, UserHomePage
from resources.movielist import CreateList, EditList, ViewList


# Each resource created under resources/ that we want to use should be added here,
# create_app() will then call the init_app() function on app.py to set them up.
# This makes the app file look much cleaner & more organized.
def init_app(app):

    api = Api(app)

    # User resources
    api.add_resource(UserListResource, "/users")
    api.add_resource(UserResource, "/users/<string:username>")
    api.add_resource(MeResource, "/me")

    # Auth resources
    api.add_resource(LoginResource, "/auth/login")
    api.add_resource(LogoutResource, "/auth/logout")
    api.add_resource(RegisterResource, "/auth/register")

    # Page resources
    api.add_resource(HomePage, "/")
    api.add_resource(LoginPage, "/login/")
    api.add_resource(RegisterPage, "/register/")
    api.add_resource(MovieList, "/movie-lists/")  # Kaikki listat näkyy tästä

    # Movielist resources
    api.add_resource(ViewList, "/users/<string:username>/list")
    api.add_resource(CreateList, "/users/<string:username>/create")
    api.add_resource(EditList, "/users/<string:username>/<int:list_id>/edit")

