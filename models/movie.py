from extensions import db


class Movie(db.Model):
    __tablename__ = "movie"

    id = db.Column(db.String(), primary_key=True)
    movie_title = db.Column(db.String(256))
    image_url = db.Column(db.String(256))
    imdb_rating = db.Column(db.String(10))
    release_year = db.Column(db.String(4))

    is_publish = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False,
                           server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False,
                           server_default=db.func.now(), onupdate=db.func.now())

    @classmethod
    def get_all_published(cls):
        return cls.query.filter_by(is_publish=True).all()

    @classmethod
    def get_by_id(cls, movie_id):
        return cls.query.filter_by(id=movie_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
