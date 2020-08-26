from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet

from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pet_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS']= False

debug = DebugToolbarExtension(app)
 
connect_db(app)
db.create_all()

@app.route('/')
def show_index():
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
        flash(f"{name}-{species}-{age}-{notes}-{url}")
        return redirect('/')
    else:
        return render_template("add_pet_form.html", form=form)
    
   
