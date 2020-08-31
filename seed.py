"""send file to make sample for pet_db"""
from models import Pet, db
from app import app

db.create_all()


p1 = Pet(name="Woofly", species="dog", photo_url="http://curric.rithmschool.com/springboard/exercises/flask-adopt/_images/screen.png", age="2", notes="born on July 4th, super energetic", available=True)

p2 = Pet(name="Porchetta", species="porcupine", photo_url="http://curric.rithmschool.com/springboard/exercises/flask-adopt/_images/screen.png", age="1", notes="born on Feb 14th, super quiet", available=False)

p3 = Pet(name="Snargle", species="cat", photo_url="http://curric.rithmschool.com/springboard/exercises/flask-adopt/_images/screen.png", age="4", notes="born on Dec 25th, super noisy", available=True)

db.session.add_all([p1, p2, p3])
db.session.commit()

