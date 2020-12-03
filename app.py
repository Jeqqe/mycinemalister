from flask import Flask

from config import Config
import resources, extensions

def create_app():

    app = Flask(__name__)
    app.config.from_object(Config)

    # Defines all the extensions that the application uses (extensions/__init__.py)
    extensions.init_app(app)

    # Defines all the flask Resources we're using on the app (resources/__init__.py)
    resources.init_app(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
