from flask import Blueprint, render_template, redirect, url_for, flash, abort
from flask import current_app as app
from flask_wtf import FlaskForm
from flask_login import login_required
from wtforms import StringField, SubmitField, PasswordField, HiddenField, TextAreaField
from wtforms.validators import DataRequired, URL
import requests
import json
import time
from datetime import datetime as dt
from datetime import timedelta
from app.models import db, Post
from app.forms import PostForm



posts_bp = Blueprint(
    'posts_bp', __name__,
    template_folder='templates',
    static_folder='static')


@posts_bp.route('/post/<index>', endpoint='posts', methods=['GET'])
def render_post():
    return render_template('post.html')

@login_required
@posts_bp.route('/new-post', endpoint='new_post', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post()
        post.title = form.title.data
        post.content = form.content.data
        timestamp = dt.now().strftime("%b, %d, %Y")
        post.time = timestamp
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('posts_bp.all_posts'))
    return render_template('new-post.html', form=form)

@posts_bp.route('/all-posts', endpoint='all_posts', methods=['GET', 'POST'])
def all_posts():
    return render_template('all-posts.html')




