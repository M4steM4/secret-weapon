from flask_security import Security, SQLAlchemyUserDatastore
from flask_compress import Compress

from backtester.data.models import db, Role, User

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SECURITY_REGISTERABLE = True
    SECURITY_REGISTER_URL = '/register'
    SECURITY_SEND_REGISTER_EMAIL = False
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml', \
    'application/json', 'application/javascript']
    COMPRESS_LEVEL = 6
    COMPRESS_MIN_SIZE = 500


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True


config = {
    "development": "backtester.config.DevelopmentConfig",
    "testing": "backtester.config.TestingConfig",
    "default": "backtester.config.DevelopmentConfig"
}

def configure_app(app):
    app.config.from_object(config['default'])

    # Configure Security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security = Security(app, user_datastore)

    # Configure Compressing
    Compress(app)
