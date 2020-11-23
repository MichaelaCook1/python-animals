from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError


from application.models import Animals

class AnimalForm(FlaskForm):
    name=StringField('name')
    noise=StringField('noise')
    submit = SubmitField('Submit')
