from extensions import db

class MovieList(db.Model):
    __tablename__ = "movielist"

    id = db.Column(db.Integer, primary_key=True)

    # Jotai tähä

    is_publish = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(), nullable=False, server_default = db.func.now())
    updated_at = db.Column(db.DateTime(), nullable=False, server_default = db.func.now(), onupdate = db.func.now())
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))

    def data(self):
        return {
            'id': self.id,
            'user_id': self.user_id
        }

    @classmethod
    def get_all_published(cls):
        return cls.query.filter_by(is_publish=True).all()

    @classmethod
    def get_by_id(cls, instruction_id):
        return cls.query.filter_by(id=instruction_id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()