from flask import Blueprint, current_app, render_template

from backtester.main.views import Main

main = Blueprint('main', __name__, template_folder='templates')

@main.route('/')
def display_index():
    return render_template("main_index.html")
