from extensions import db

class Review(db.Model):
    __tablename__ = "review"

    id = db.Column(db.Integer, primary_key=True)
    user_rating = db.Column(db.String(10))
    user_review = db.Column(db.String(1000))

    is_publish = db.Column(db.Boolean(), default=True)
    created_at = db.Column(db.DateTime(), nullable=False,
                           server_default=db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False,
                           server_default=db.func.now(), onupdate=db.func.now())

    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))
    movie_id = db.Column(db.String(), db.ForeignKey("movie.id"))

    @classmethod
    def get_all_published(cls):
        return cls.query.filter_by(is_publish=True).all()

    @classmethod
    def get_by_id(cls, review_id):
        return cls.query.filter_by(id=review_id).first()

    @classmethod
    def get_reviews_from_user(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def edit(self, review, rating):

        self.user_review = review
        self.user_rating = rating
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
