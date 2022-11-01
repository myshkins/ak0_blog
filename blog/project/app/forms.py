from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, HiddenField, TextAreaField
from wtforms.validators import DataRequired, URL



class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("login")

class PostForm(FlaskForm):
    title = StringField("title", validators=[DataRequired()])
    content = TextAreaField("content", validators=[DataRequired()])
    submit = SubmitField("submit")
