"""model for pet_adoption"""

from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def connect_db(app):
    """connect to db"""

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pet model"""
    __tablename__ = "pets"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    photo_url= db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    notes = db.Column(db.Text, nullable=False)
    available = db.Column(db.Text, nullable=False)

