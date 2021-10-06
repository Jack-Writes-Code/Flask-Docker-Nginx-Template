from flask_sqlalchemy       import SQLAlchemy

db = SQLAlchemy()

class Example_Model(db.Model):
    __tablename__ = 'API_requests_tracker'
    id                      = db.Column(db.Integer, primary_key=True)
    ip_address              = db.Column(db.Text)
    method                  = db.Column(db.Text)
    requests                = db.Column(db.Integer)