from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):

    name = StringField("name", validators=[InputRequired(message="Pet name can't be blank")])
    species = StringField("species",validators=[InputRequired(message="Species can't be blank")])
    url = StringField("photo_url", validators=[Optional()])
    age = IntegerField("age", validators=[Optional()])
    notes = StringField("notes", validators=[Optional()])