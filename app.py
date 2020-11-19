from flask import Flask

from config import Config
import resources, extensions

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    extensions.init_app(app)
    resources.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()

    #print(Movie().searchMovie("Shrek"))