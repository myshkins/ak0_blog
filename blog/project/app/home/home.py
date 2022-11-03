from flask import Blueprint, render_template, redirect, url_for, session, jsonify, request
from flask import current_app as app
from flask_wtf import FlaskForm
from flask_login import login_user, LoginManager, login_required, current_user, logout_user
from wtforms import StringField, SubmitField, PasswordField, HiddenField
from wtforms.validators import DataRequired, URL
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import json
import time
from datetime import datetime as dt
from datetime import timedelta
from app.models import db, Post, User, Likes
import markdown
import logging


logging.basicConfig(filename='blog_log.txt', level=logging.DEBUG)

home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static')

def get_session_data():
    data = [x for x in session.items()]
    return data


@home_bp.route('/', endpoint='home', methods=['GET'])
def home():
    query = Post.query.limit(5).all()
    posts = []
    for post in query:
        title = post.title
        post_id = post.id
        md = markdown.markdown(post.content)
        end_ind = md.find('</p>')
        blurb = md[3:end_ind]
        posts.append((title, post_id, blurb))
    likes = Likes.query.first()
    num_likes = likes.number
    data = {item[0]:item[1] for item in get_session_data()}
    return render_template(
        'index.html',
        posts=posts,
        logged_in=current_user.is_active, 
        likes=num_likes, 
        data=data
        )

@home_bp.route('/like', endpoint='like', methods=['GET'])
def like():
    likes = Likes.query.first()
    if 'liked' in list(session.items()):
        return jsonify({'likes': likes.number})
    else:
        likes.number += 1
        session['liked'] = 'liked'
        db.session.commit()
        return jsonify({'likes': likes.number})

@home_bp.route('/first-like', endpoint='first-like', methods=['GET'])
def first_like():
    likes = Likes()
    likes.number = 1
    db.session.add(likes)
    db.session.commit()
    return redirect(url_for('home_bp.home'))