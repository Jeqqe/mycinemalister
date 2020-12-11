from flask import make_response, render_template, request, redirect
from flask_login import current_user
from flask_restful import Resource

from extensions import imdb
from models.movie import Movie
from models.review import Review


class EditList(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('edit_list.html'), 200, headers)


class MovieList(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('movie_lists.html'), 200, headers)


class ViewList(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}

        reviews = Review.get_reviews_from_user(current_user.id)
        result = []
        for review in reviews:

            movie_info = Movie.get_by_id(review.movie_id)
            result.append(
                {
                    "review_id": review.id,
                    "movie_title": movie_info.movie_title,
                    "image_url": movie_info.image_url,
                    "imdb_rating": movie_info.imdb_rating,
                    "release_year": movie_info.release_year,
                    "user_rating": review.user_rating,
                    "user_review": review.user_review
                }
            )

        return make_response(render_template('view_list.html', movies=result, lenght=len(result)), 200, headers)


class SearchMovie(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('search_movie.html'), 200, headers)

    # Load the search results to the page
    def post(self):

        movie_title = request.form['movie_title']
        search_results = None
        error = None

        if len(movie_title) < 2:
            error = "Search has to be atleast 2 characters long"
        else:
            search_results = imdb.searchMovie(movie_title)

            if "Error" in search_results:
                error = search_results["Error"]

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('search_movie.html', error= error, search_results = search_results), 200, headers)


class CreateMovieReview(Resource):

    # Load the search results to the page
    def get(self, movie_id):

        movie = Movie.get_by_id(movie_id)

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('new_review.html', movie=movie), 200, headers)

    def post(self, movie_id):

        form = request.form

        Review(
            user_rating=form["rating"],
            user_review=form["review"],
            user_id=current_user.id,
            movie_id=movie_id
           ).save()

        return redirect("/")


class EditMovieReview(Resource):

    # Load the search results to the page
    def get(self, review_id):

        review = Review.get_by_id(review_id)
        movie = Movie.get_by_id(review.movie_id)

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('edit_review.html', movie=movie, review=review), 200, headers)

    def post(self, review_id):

        form = request.form

        review = Review.get_by_id(review_id)
        review.edit(review=form["review"], rating=form["rating"])

        return redirect("/reviews/mine")
