from flask import make_response, render_template, request
from flask_restful import Resource

from extensions import imdb


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
        testMovie = {
            # Nämä tiedot tulisi api:sta tai tietokannasta:
            'movie_title': 'Shrek',
            'image_url': 'https://m.media-amazon.com/images/M/MV5BOGZhM2FhNTItODAzNi00YjA0LWEyN2UtNjJlYWQzYzU1MDg5L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY1200_CR88,0,630,1200_AL_.jpg',
            'imdb_rating': '8,5/10',
            'release_year': '2012',
            # Nämä kaks tulis movielist taulusta:
            'user_rating': '10/10',
            'user_comment': 'Dis my rating. If u no like shrek u gey. Shrek best movie ever. plz watch shrek if u havent seen. shrek best.'
        }

        return make_response(render_template('view_list.html', movies=testMovie), 200, headers)


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



