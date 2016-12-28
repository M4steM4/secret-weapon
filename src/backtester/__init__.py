from flask import abort, Flask, g, render_template, request

from backtester.config import configure_app
from backtester.main.controllers import main


app = Flask(__name__,
            template_folder='templates')

configure_app(app)


app.register_blueprint(main, url_prefix='/')
