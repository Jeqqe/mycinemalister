from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# All the extension related stuff we need to initialize when the app starts go here
def init_app(app):

    db.init_app(app)
    Migrate(app, db)

