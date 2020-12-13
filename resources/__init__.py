from flask import make_response, render_template
from flask_restful import Api

from resources.auth import Login, Logout, Register
from resources.page import HomePage
from resources.movie import UserMovieReviews, MovieList, SearchMovie, CreateMovieReview, EditMovieReview, DeleteMovieReview


# Each resource created under resources/ that we want to use should be added here,
# create_app() will then call the init_app() function on app.py to set them up.
# This makes the app file look much cleaner & more organized.


def init_app(app):

    api = Api(app)

    # Auth resources
    api.add_resource(Login, "/auth/login")
    # login_required
    api.add_resource(Logout, "/auth/logout")
    api.add_resource(Register, "/auth/register")

    # Page resources
    api.add_resource(HomePage, "/")

    # Movie/review resources
    api.add_resource(MovieList, "/reviews/all")
    # login_required
    api.add_resource(SearchMovie, "/reviews/create")
    # login_required
    api.add_resource(UserMovieReviews, "/reviews/mine")

    # login_required
    api.add_resource(CreateMovieReview, "/reviews/new/<string:movie_id>")
    # login_required # ownership of review required
    api.add_resource(EditMovieReview, "/reviews/edit/<string:review_id>")
    # login_required # ownership of review required
    api.add_resource(DeleteMovieReview, "/reviews/delete/<string:review_id>")



    # Unauthorized access handler
    @app.login_manager.unauthorized_handler
    def unauthorized_callback():
        headers = {'Content-Type': 'text/html'}
        error_message = "Unauthorized access, please login before accessing this page."
        return make_response(render_template('error.html', error_message=error_message), 401, headers)