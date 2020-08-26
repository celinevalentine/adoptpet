from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtform.validators import InputRequired, Email, Optional

class AddPetForm(FlaskForm):
    name = StringField("Pet name", validators=[InputRequired(message="Pet name can't be blank")])
    species = StringField("Species",validators=[InputRequired(message="Species can't be blank")])
    url = StringField("Photo URL", validators=[Optional()])
    age = IntegerField("Age", validators=[Optional()])
    notes = StringField("Notes", validators=[Optional()])