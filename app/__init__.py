from flask import Flask

# from flask_wtf.csrf import CSRFProtect

from app.index.views import index_bp
from app.db.database import MySQLDatabaseSingleton

from app.index.models import Verb

app = Flask(__name__)

# csrf = CSRFProtect()

database = MySQLDatabaseSingleton().database


def create_app(config):
    """
    Creates and configures the Flask application.

    Args:
        config (str): The name of the configuration class to use for the Flask
        application.

    Returns:
        The configured Flask application instance.
    """

    app.config.from_object(config)

    # csrf.init_app(app)

    app.register_blueprint(index_bp)
    
    with app.app_context():
        database.create_tables([Verb], safe=True)

    return app