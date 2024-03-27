from . import db
from datetime import datetime

class Todobase(db.Model):
    __tablename__ = "todobase"
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String, nullable=False)
    task_stat = db.Column(db.String, nullable=False)
    task_cat = db.Column(db.String, nullable=False)
    task_project = db.Column(db.String, nullable=False)
    descript = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Todobase %r>' %self.id
