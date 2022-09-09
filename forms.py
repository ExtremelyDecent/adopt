from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional


class AddPetForm(FlaskForm):
    """ Form for adding pet"""

    name = StringField(
        "Pet Name",
        validators = [InputRequired()],
    )

    species = SelectField(
        "Species",
        choices = [("cat", "Cat"), ("dog" ,"Dog"), ("fish", "Fish"), ("hamster", "Hamster"), ("snake","Snake")],
    )

    photo_url = StringField(
        "Photo URL",
        validators = [Optional(), URL()],
    )

    age = IntegerField(
        "Age",
        validators = [Optional(), NumberRange(min = 0, max = 45)],
    )

    notes = TextAreaField(
        "Notes",
        validators = [Optional(), Length(min=10)],
    )

class EditPetForm(FlaskForm):
    """form for editing existing pets"""

    photo_url = StringField(
        "Photo URL",
        validators = [Optional(), URL()],
    )    
    notes = TextAreaField(
        "Notes",
        validators = [Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")