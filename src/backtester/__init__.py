from flask import abort, Flask, g, render_template, request
from flask_security import current_user
from flask_babel import Babel

from htmlmin.main import minify

from backtester.data.models import db
from backtester.config import configure_app

from backtester.dashboard.controllers import dashboard
from backtester.setting.controllers import setting


app = Flask(__name__,
            template_folder='templates')

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

@app.after_request
def response_minify(response):
    """
    minify html response to decrease site traffic
    """
    if response.content_type == u'text/html; charset=utf-8':
        response.set_data(
            minify(response.get_data(as_text=True))
        )

        return response
    return response

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('Page not found: %s', (request.path, error))
    return render_template('404.html'), 404

@app.context_processor
def inject_data():
    return dict(user=current_user,ang=1)

@app.route('/')
def index(lang_code=None):
    return render_template('index.html')


app.register_blueprint(dashboard, url_prefix='/dashboard')
app.register_blueprint(setting, url_prefix='/setting')
