from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class AddRecipeForm(FlaskForm):
  recipe_name = StringField('Recipe Name', validators=[DataRequired()])
  recipe_intro = TextAreaField('Recipe Intro', validators=[DataRequired()])
  ingredients = TextAreaField('Ingredients (one per line please)', validators=[DataRequired()])
  method = TextAreaField('Method', validators=[DataRequired()])
  image = StringField('Image Link (Full Path)', validators=[DataRequired()])
  submit = StringField('Update Recipe')

class EditRecipeForm(FlaskForm):
  recipe_name = StringField('Recipe Name', validators=[DataRequired()])
  recipe_intro = TextAreaField('Recipe Introduction', validators=[DataRequired()])
  ingredients = TextAreaField('Ingredients (one per line please)', validators=[DataRequired()])
  method = TextAreaField('Method', validators=[DataRequired()])
  image = StringField('Image Link (full path)', validators=[DataRequired()])
  Submit = SubmitField('Update Recipe')

class ConfirmDelete(FlaskForm):
  recipe_name = StringField('Recipe Name', validators=[DataRequired()])
  submit = SubmitField('Delete this Recipe')





