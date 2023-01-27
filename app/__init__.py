import os
import logging
from flask import Flask, request
from flask_babel import Babel
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from logging.handlers import RotatingFileHandler
from flask_login import LoginManager
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask_babel import lazy_gettext as _l

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
moment = Moment(app)

login = LoginManager(app)
login.login_view = 'login'
login.login_message = _l('Você precisa estar logado para acessar esta página.')

if not app.debug:
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

from app import routes, errors
from app.modules import models

bootstrap = Bootstrap(app)

babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])