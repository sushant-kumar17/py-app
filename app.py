from flask import Flask
from dotenv import load_dotenv
from config import Config
from extensions import db, migrate

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    from routes.auth import auth_bp
    from routes.book import book_bp
    from routes.homepage import homepage_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(book_bp, url_prefix='/books')
    app.register_blueprint(homepage_bp, url_prefix='/')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
