from app import db

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.Date)
    end = db.Column(db.Date)
    title = db.Column(db.String(120))