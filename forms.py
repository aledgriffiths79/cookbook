from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class AddRecipeForm(FlaskForm):
  recipe_name = StringField('Recipe Name', validators=[DataRequired()])
  short_description = TextAreaField('Short Description', validators=[DataRequired()])
  ingredients = TextAreaField('Ingredients (one per line please)', validators=[DataRequired()])
  method = TextAreaField('Method', validators=[DataRequired()])
  image = StringField('Image Link (Full Path)', validators=[DataRequired()])
  submit = StringField('Update Recipe')

