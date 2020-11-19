import requests

class Movie:

    api = "https://imdb-api.com/en/API/"
    key = "k_rn5hp3uz"

    # Requests movies that match search result
    def searchMovie(self, to_search_for):
        req = requests.get(self.api + f"SearchMovie/{self.key}/{to_search_for}").json()
        return req



