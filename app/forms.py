from flask_wtf import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

class VariantSubmitForm(Form):
    chromosome = StringField('Chromosome', validators=[DataRequired()])
    position = StringField('Position', validators=[DataRequired()])
    ref = StringField('Ref', validators=[DataRequired()])
    alt = StringField('Alt', validators=[DataRequired()])