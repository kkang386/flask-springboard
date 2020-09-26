from project import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

#from flask_sqlalchemy import SQLAlchemy
#db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50))

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    views = db.Column(db.Integer, nullable = False)
    likes = db.Column(db.Integer, nullable = False)
    
    def __repr__(self):
        print (self.name)
        return f"Video(name={self.name}, views={self.views}, likes={self.likes})"

