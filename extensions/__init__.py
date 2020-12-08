from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from imdb.movie import IMDB

db = SQLAlchemy()
login_manager = LoginManager()
imdb = IMDB()

# All the extension related stuff we need to initialize when the app starts go here
def init_app(app):

    db.init_app(app)
    Migrate(app, db)

    from models.user import User
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get_by_id(user_id)