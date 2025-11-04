from src.app import create_app
from src.database import db


def init_database():
    app = create_app()
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    init_database()
    print("Database initialized.")
