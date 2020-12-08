import requests

# Handles all imdb api related stuff
class IMDB:

    api = "https://imdb-api.com/en/API/"
    key = "k_rn5hp3uz"

    # Requests additional info about the movie
    def getMoreInfo(self, movie_id):
        return requests.get(self.api + f"Title/{self.key}/{movie_id}").json()


    # Requests movie ids that match the search keyword(s)
    def searchMovie(self, to_search_for):
        from models.movie import Movie as db

        req = requests.get(self.api + f"SearchMovie/{self.key}/{to_search_for}").json()

        if req["errorMessage"] != "":
            return "Something went wrong, no movies found."

        results = {}
        for result in req["results"]:
            movie_id = result["id"]

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
            info = self.getMoreInfo(movie_id)
            results[movie_id] = {
                "title": info["title"],
                "image_url": info["image"],
                "release": info["year"],
                "imdb_rating": info["imDbRating"]
            }

            db(id=movie_id,
               movie_title=results[movie_id]["title"],
               image_url=results[movie_id]["image_url"],
               imdb_rating=results[movie_id]["release"],
               release_year=results[movie_id]["imdb_rating"]
               ).save()

        return results
