from flask import Flask, request, redirect, render_template, flash, url_for
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']= False

debug = DebugToolbarExtension(app)
 
connect_db(app)
db.create_all()

@app.route('/')
def list_pets():
    """show homepage"""
    pets = Pet.query.all()
    return render_template('index.html', pets=pets)

@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """submit the form to add a pet"""
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        url = form.url.data
        age = form.age.data
        notes = form.notes.data
        pet = Pet(name=name, species=species, photo_url=url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()
        flash(f"{pet.name} is added.")
        return redirect(url_for('list_pets'))
    else:
        return render_template("add_pet_form.html", form=form)

@app.route('/<int:id>', methods=["GET", "POST"])
def edit_pet(id):
    """edit pet info for a specific pet"""
    pet = Pet.query.get_or_404(id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.notes = form.notes.data
        pet.photo_url = form.url.data
        pet.available = form.available.data
        db.session.commit()
        flash(f"{pet.name} is updated.")
        return redirect(url_for('list_pets'))
    else:
        return render_template("edit_pet_form.html",form=form, pet=pet)