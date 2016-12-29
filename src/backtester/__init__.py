from flask import abort, Flask, g, render_template, request
from flask_security import current_user
from flask_babel import Babel

from backtester.data.models import db
from backtester.config import configure_app
from backtester.main.controllers import main


app = Flask(__name__,
            template_folder='templates')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

babel = Babel(app)
configure_app(app)
db.init_app(app)

app.jinja_env.add_extension('jinja2.ext.loopcontrols')

@babel.localeselector
def get_locale():
    return g.get('lang_code', app.config['BABEL_DEFAULT_LOCALE'])

@babel.timezoneselector
def get_timezone():
    user = g.get('user', None)
    if user is not None:
        return user.timezone

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('Page not found: %s', (request.path, error))
    return render_template('404.html'), 404

@app.context_processor
def inject_data():
    print(dir(current_user))
    return dict(user=current_user,ang=1)

@app.route('/')
def index(lang_code=None):
    return render_template('index.html')

app.register_blueprint(main, url_prefix='/main')
