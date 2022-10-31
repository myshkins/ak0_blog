from flask import Blueprint, render_template, redirect, url_for, flash, abort, g
from flask import current_app as app
from flask_wtf import FlaskForm
from flask_login import login_user, LoginManager, login_required, current_user, logout_user
from wtforms import StringField, SubmitField, PasswordField, HiddenField
from wtforms.validators import DataRequired, URL
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from app.models import db, Post, User



auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static')


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("login")

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth_bp.route('/login', endpoint='login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('auth'), logged_in=current_user.is_active)
    return render_template('login.html', form=form)


@auth_bp.route('/register', endpoint='register', methods=["POST", "GET"])
def register():
    form = LoginForm()
    if form.validate_on_submit():
        password = form.password.data
        username = form.username.data
        with open('auth.txt') as file:
            hsh = file.read()
            if check_password_hash(hsh, password) and username == 'myshkins':
                user = User()
                user.username = form.username.data
                user.password = generate_password_hash(form.password.data, method="pbkdf2:sha256", salt_length=8)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                flash(f"Welcome, {user.username}")
            return render_template("register.html", registered=current_user.is_active)
    return render_template("register.html", form=form, registered=current_user.is_active)