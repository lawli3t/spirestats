from flask import Flask
from flask import _app_ctx_stack


def create_app(config_filename: str) -> Flask:
    app = Flask(__name__)

    from app.commands.importer import blueprint as extract_blueprint
    app.register_blueprint(extract_blueprint)

    @app.teardown_appcontext
    def close_connection(exception):
        top = _app_ctx_stack.top
        if hasattr(top, 'sqlite_db'):
            top.sqlite_db.close()

    return app
