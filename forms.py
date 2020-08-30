from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length


class AddPetForm(FlaskForm):
    """form for adding a pet"""

    name = StringField(
        "name", 
        validators=[InputRequired(message="Pet name can't be blank")])
    species = SelectField(
        "species",
       choices= [("cat","cat"), ("dog", "dog"), ("porcupine", "porcupine")])
    url = StringField(
        "photo_url", 
        validators=[Optional(), URL()])
    age = IntegerField(
        "age",
        validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField(
        "notes",
        validators=[Optional(), Length(min=10)])
    

class EditPetForm(FlaskForm):

    url = StringField(
        "photo_url", 
        validators=[Optional(), URL()])
    notes = TextAreaField(
        "notes",
        validators=[Optional(), Length(min=10)])
    available = BooleanField("Available?")