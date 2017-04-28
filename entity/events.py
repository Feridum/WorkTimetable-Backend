from app import db

class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    start = db.Column(db.Date)
    end = db.Column(db.Date)
    title = db.Column(db.String(120))

    def __init__(self, start,end,title):
        self.start = start
        self.end = end
        self.title = title

    def serialize(self):
        return{
            'id': self.id,
            'start':self.start,
            'end': self.end,
            'title':self.title
        }