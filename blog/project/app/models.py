from app import db

class Post(db.Model):
    """Data model for blog posts."""

    __tablename__ = 'posts'
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    title = db.Column(
        db.String,
        unique=True,
        nullable=False,
    )
    content = db.Column(
        db.Text,
        unique=False,
        nullable=False
    )
    time = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=False
    )
    updated = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True
    )

    def __repr__(self):
        return '<User {}>'.format(self.username)
