from flask import Flask
from flask import _app_ctx_stack

from app.database import DB_ATTRIBUTE


def create_app(config_filename: str) -> Flask:
    app = Flask(__name__)

    from app.commands.importer import blueprint as extract_blueprint
    app.register_blueprint(extract_blueprint)

    from app.controller import relic
    app.register_blueprint(relic)

    @app.teardown_appcontext
    def close_connection(exception):
        top = _app_ctx_stack.top
        if hasattr(top, DB_ATTRIBUTE):
            getattr(top, DB_ATTRIBUTE).close()

    return app
