from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Import all the models that we wish to use with the db so flask knows where to look for them
from models import user
from models import movie_list

# All the extension related stuff we need to initialize when the app starts go here
def init_app(app):

    db.init_app(app)
    Migrate(app, db)

