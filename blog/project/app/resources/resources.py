from flask import Blueprint, render_template
from flask import current_app as app
from flask import Blueprint, render_template
from flask import current_app as app
import requests

resources_bp = Blueprint(
    'resources_bp', __name__,
    template_folder='templates',
    static_folder='static')

@resources_bp.route('/about', endpoint='resources', methods=['GET'])
def about():
    return render_template('about.html')

@resources_bp.route('/contents', endpoint='contents', methods=['GET'])
def contents():
    return render_template('contents.html')

@resources_bp.route('/contact', endpoint='contact', methods=['GET'])
def contact():
    return render_template('contact.html')


