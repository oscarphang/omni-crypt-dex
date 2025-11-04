from .database import db


class ApiClient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    api_key = db.Column(db.String(64), unique=True, nullable=False)
    api_secret = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return f'<ApiClient {self.id}>'

class DexConnection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    api_client_id = db.Column(db.Integer, db.ForeignKey('api_client.id'), nullable=False)
    dex_name = db.Column(db.String(64), nullable=False)
    api_key = db.Column(db.String(128))
    api_secret = db.Column(db.String(256))

    api_client = db.relationship('ApiClient', backref=db.backref('dex_connections', lazy=True))

    def __repr__(self):
        return f'<DexConnection {self.dex_name}>'
