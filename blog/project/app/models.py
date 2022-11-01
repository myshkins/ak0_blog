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
    comments = db.relationship("Comment", back_populates='posts')
    def __repr__(self):
        return '<Post {}>'.format(self.title)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(250), nullable=False)
    comments = db.relationship('Comment', back_populates='users')
    def __repr__(self):
        return '<User {}>'.format(self.username)


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(500), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    users = db.relationship('User', back_populates='comments')
    posts = db.relationship('Post', back_populates='comments')
    def __repr__(self):
        return '<Comment {}>'.format(self.id)