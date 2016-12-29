from flask import Blueprint, current_app, render_template
from flask_security.decorators import login_required

from backtester.dashboard.views import Main

dashboard = Blueprint('dashboard', __name__, template_folder='templates')

@dashboard.route('/')
@login_required
def display_index():
    return render_template("dashboard_index.html")
