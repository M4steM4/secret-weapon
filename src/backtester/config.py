from flask_security import Security, SQLAlchemyUserDatastore
from flask_login import LoginManager
from backtester.data.models import db, Role, User

class BaseConfig(object):
    DEBUG = False
    TESTING = False


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
