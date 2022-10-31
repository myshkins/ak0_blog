from app import db
from flask_login import UserMixin

class Post(db.Model):
    """Data model for blog posts."""

    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False,)
    content = db.Column(db.Text, unique=False, nullable=False)
    time = db.Column(db.DateTime, index=False, unique=False, nullable=False)
    updated = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    def __repr__(self):
        return '<Post {}>'.format(self.title)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    # comments = relationship("Comment", back_populates="users")
    def __repr__(self):
        return '<User {}>'.format(self.username)