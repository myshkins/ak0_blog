from flask import Blueprint, render_template, redirect, url_for, flash, abort
from flask import current_app as app
from flask_wtf import FlaskForm
from flask_login import login_required, current_user
from wtforms import StringField, SubmitField, PasswordField, HiddenField, TextAreaField
from wtforms.validators import DataRequired, URL
import requests
import json
from datetime import datetime as dt
from datetime import timedelta
from app.models import db, Post
from app.forms import PostForm
import markdown



posts_bp = Blueprint(
    'posts_bp', __name__,
    template_folder='templates',
    static_folder='static')


@posts_bp.route('/post/<int:post_id>', endpoint='render_post', methods=['GET', 'POST'])
def render_post(post_id):
    requested_post = Post.query.get(post_id)
    title = requested_post.title
    content = markdown.markdown(requested_post.content)
    post_id = requested_post.id
    return render_template(
        'post.html',
        title=title,
        content=content,
        post_id=post_id,
        logged_in=current_user.is_active
        )

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
    return render_template(
        'new-post.html',
        form=form,
        logged_in=current_user.is_active
        )

@posts_bp.route('/all-posts', endpoint='all_posts', methods=['GET', 'POST'])
def all_posts():
    titles = [
        (title, post_id) for title, post_id in 
        db.session.query(Post.title, Post.id)]
    return render_template(
        'all-posts.html',
        titles=titles,
        logged_in=current_user.is_active
        )

@login_required
@posts_bp.route('/edit-post/<int:post_id>', endpoint='edit_post', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get(post_id)
    form = PostForm(title=post.title, content=post.content)
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        timestamp = dt.now().strftime("%b, %d, %Y")
        post.updated = timestamp
        db.session.commit()
        return redirect(
            url_for('posts_bp.render_post',
            post_id=post_id,
            logged_in=current_user.is_active)
            )
    return render_template(
        'edit-post.html',
        post_id=post_id,
        form=form,
        logged_in=current_user.is_active
        )

