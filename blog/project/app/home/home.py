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



home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static')


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("login")


def admin_only(func):
    @wraps(func)
    def decorated_func(*args, **kwargs):
        if current_user.id != 1:
            abort(403)
        else:
            return func(*args, **kwargs)
    return decorated_func



@home_bp.route('/', endpoint='home', methods=['GET'])
def home():
    return render_template('index.html', )#logged_in=current_user.is_active)


@home_bp.route('/login', endpoint='login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('home'), logged_in=current_user.is_active)
    return render_template('login.html', form=form)

@app.route('/register', methods=["POST", "GET"])
def register():
    form = UserForm()
    if form.validate_on_submit():
        with open('auth.txt') as file:
            hsh = file.read()
            if check_password_hash(hsh, password) and username == 'myshkins':
                user = User()
                user.username = form.username.data
                user.password = generate_password_hash(form.password.data, method="pbkdf2:sha256", salt_length=8)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                flash(f"Welcome, {user.name}")
            return render_template("register.html", registered=current_user.is_active)
    return render_template("register.html", form=form, registered=current_user.is_active)