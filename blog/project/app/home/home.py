from flask import Blueprint, render_template, redirect, url_for
from flask import current_app as app
import requests
import json
from io import BytesIO
import time
from datetime import datetime as dt
from datetime import timedelta
from app.models import db, Post



home_bp = Blueprint(
    'home_bp', __name__,
    template_folder='templates',
    static_folder='static')


@home_bp.route('/', endpoint='home', methods=['GET'])
def home():
    return render_template('index.html')

