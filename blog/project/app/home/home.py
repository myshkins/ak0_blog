from flask import Blueprint, render_template, redirect, url_for, flash, abort, g
from flask import current_app as app
from flask_wtf import FlaskForm
from flask_login import login_user, LoginManager, login_required, current_user, logout_user
from wtforms import StringField, SubmitField, PasswordField, HiddenField
from wtforms.validators import DataRequired, URL
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import requests
import json
import time
from datetime import datetime as dt
from datetime import timedelta
from app.models import db, Post, User
import markdown



home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static')


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
    return render_template(
        'index.html',
        posts=posts,
        logged_in=current_user.is_active
        )


