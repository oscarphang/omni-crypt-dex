import logging

from flask import Flask

from .config import Config


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    from .database import db
    db.init_app(app)

    from .routes.prices import prices_bp
    app.register_blueprint(prices_bp)

    from .routes.orders import orders_bp
    app.register_blueprint(orders_bp)

    from .routes.balances import balances_bp
    app.register_blueprint(balances_bp)

    @app.route('/')
    def index():
        return "<h1>Crypto DEX API</h1>"

    return app
