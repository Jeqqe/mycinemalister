import requests

# Handles all imdb api related stuff
class IMDB:

    api = "http://www.omdbapi.com/?apikey="
    key = "2debe9fe"

    # Requests additional info about the movie
    def getImdbRating(self, movie_id):

        return requests.get(self.api + f"{self.key}&i={movie_id}&type=movie").json()

    # Requests movie ids that match the search keyword(s)
    def searchMovie(self, to_search_for):
        from models.movie import Movie as db

        #print(self.api + f"{self.key}&s={to_search_for}&type=movie")
        req = requests.get(self.api + f"{self.key}&s={to_search_for}&type=movie").json()

        if req["Response"] == "False":
            return req

        results = {}
        for result in req["Search"]:
            movie_id = result["imdbID"]

            # If movie is already in db, use the data from there
            info = db.get_by_id(movie_id)
            if info:
                results[movie_id] = {
                    "title": info.movie_title,
                    "image_url": info.image_url,
                    "release": info.release_year,
                    "imdb_rating": info.imdb_rating
                }
                continue

            # If movie not in db, request it from the api & add to the database
            info = self.getImdbRating(movie_id)
            if info["Response"] == "False":
                return req

            results[movie_id] = {
                "title": result["Title"],
                "image_url": info["Poster"],
                "release": info["Year"],
                "imdb_rating": info["imdbRating"]
            }

            db(id=movie_id,
               movie_title=results[movie_id]["title"],
               image_url=results[movie_id]["image_url"],
               imdb_rating=results[movie_id]["imdb_rating"],
               release_year=results[movie_id]["release"]
               ).save()

        return results