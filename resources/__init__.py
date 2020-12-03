from flask_restful import Api

from resources.token import TokenResource, RefreshResource, RevokeResource
from resources.user import UserListResource, UserResource, MeResource
from resources.page import HomePage, LoginPage, RegisterPage, MovieList, UserHomePage


# Each resource created under resources/ that we want to use should be added here,
# create_app() will then call the init_app() function on app.py to set them up.
# This makes the app file look much cleaner & more organized.
def init_app(app):

    api = Api(app)

    # User resources
    api.add_resource(UserListResource, "/users")
    api.add_resource(UserResource, "/users/<string:name>")
    api.add_resource(MeResource, "/me")

    # Token resources
    api.add_resource(TokenResource, "/token")
    api.add_resource(RefreshResource, '/refresh')
    api.add_resource(RevokeResource, '/revoke')

    # Page resources
    api.add_resource(HomePage, "/")
    api.add_resource(LoginPage, "/login/")
    api.add_resource(RegisterPage, "/register/")
    api.add_resource(MovieList, "/movie-lists/")
