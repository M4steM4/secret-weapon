from flask import Blueprint, current_app, render_template
from flask_security.decorators import login_required

setting = Blueprint('setting', __name__, template_folder='templates')

@setting.route('/')
@login_required
def display_index():
    return render_template("setting_index.html")
