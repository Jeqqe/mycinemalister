from flask import make_response, render_template, request, redirect
from flask_restful import Resource

# Nää on perjaattees kyl iha normi view pageja et ne vois kyl olla tuol noitte muitte pagejekaa emt.
# jos haluut siirtää nii siit vaa.


class CreateList(Resource):
    def get(self, username):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('create_list.html', username=username), 200, headers)


class EditList(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('edit_list.html'), 200, headers)


class ViewList(Resource):
    def get(self, username):
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
    def post(self, username):
        # Get movie name from search bar
        movie_title = request.form['movie_title']
        # hakee movie_title:lla sen leffan
        print(movie_title)
        # tää on vaa random redirect... redirectataan varmaan johonki /users/didzis/create/shrek
        return redirect("/users/" + username + "/lists", movie_title)
