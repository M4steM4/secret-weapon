from flask import abort, Flask, g, render_template, request

from backtester.config import configure_app


app = Flask(__name__,
            template_folder='templates')

configure_app(app)
