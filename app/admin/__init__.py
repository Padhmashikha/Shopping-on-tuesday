
from flask import Flask, render_template
from app.admin import admin

def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(admin)

    # GLOBAL 500 handler for the entire app
    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template("errors/500.html"), 500

    return app