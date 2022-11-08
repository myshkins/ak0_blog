from flask import Blueprint, render_template, send_from_directory
from flask import current_app as app
import requests

resources_bp = Blueprint(
    'resources_bp', __name__,
    template_folder='templates',
    static_folder='static')

@resources_bp.route('/about', endpoint='about', methods=['GET'])
def about():
    return render_template('about.html')

@resources_bp.route('/contact', endpoint='contact', methods=['GET'])
def contact():
    return render_template('contact.html')

# @resources_bp.route('/media/<path:filename>')
# def media_file(filename):
#     return send_from_directory(directory, filename)
