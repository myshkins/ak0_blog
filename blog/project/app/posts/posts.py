from flask import Blueprint, render_template, redirect, url_for
from flask import current_app as app
import requests
import json
import time
from datetime import datetime as dt
from datetime import timedelta
from app.models import db, Post



posts_bp = Blueprint(
    'posts_bp', __name__,
    template_folder='templates',
    static_folder='static')


@posts_bp.route('/post/<index>', endpoint='posts', methods=['GET'])
def render_post():
    return render_template('index.html')

