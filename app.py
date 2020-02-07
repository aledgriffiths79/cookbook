import os
import re
import math
from forms import AddRecipeForm, ConfirmDelete, EditRecipeForm
# from config import Config
# after deleting the above import Config, now my application is running on heroku 
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, DESCENDING
from pymongo import MongoClient
from bson.objectid import ObjectId
# the following is for the environment variable
from os import path
if path.exists('env.py'):
  import env

app = Flask(__name__)

# add configuration to our flask application
# Beacuse you set the value of MONGO_DBNAME to be "CookBook" in your environment variables. So os.getenv("MONGO_DBNAME")  will return "CookBook" as a string. the only difference is you hard coded it into line 20, rather than getting it from the environment.
app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
# app.config['MONGO_DBNAME'] = 'CookBook'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# i shouldnt upload secret keys to github thus here too, but i can leave it here for now. When i come to upload this application onto the production server (heroku), its then i put it into environment variables inside heroku itself 

# PyMongo connects to the MongoDB server running on port 27017 on localhost
# app.config["MONGO_URI"] = "mongodb://localhost:27017/recipes"

# Create an instance of pyMongo
#(app) is a app object in brackets as an argument
mongo = PyMongo(app)

# Decorators

@app.route('/')
@app.route('/index')
def index():
  """Homepage has 4 recipes from DB that have been viewed the most"""
  four_recipes = mongo.db.Recipes.find().sort([('views', DESCENDING)]).limit(4)
  return render_template('index.html', title='Home', Recipes=four_recipes)
  # below is a setting stone to if my production site works
  # return 'Hello'

# Add recipe file

@app.route('/add_recipe', methods=['GET', 'POST']) #routing identifier will have the same name as the function name (its a choice as its easier for a beginner)
def add_recipe():
  """Creates a recipe and enters into recipe collection"""
  form = AddRecipeForm(request.form)
  if request.method=='POST':
    # set the collection
    recipes_db = mongo.db.Recipes
    # insert the new recipe
    recipes_db.insert_one({
      'recipe_name': request.form['recipe_name'],
      'recipe_intro': request.form['recipe_intro'],
      'ingredients': request.form['ingredients'],
      'method': request.form['method'],
      'image': request.form['image'],
      'submit': request.form['submit'],
      'views': 0
    })
    return redirect(url_for('index', title='New Recipe Added'))
  else:
    return render_template('add_recipe.html', title='add a recipe', form=form)

# Edit Recipe

@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
  the_recipe = mongo.db.Recipes.find_one({'_id': ObjectId(recipe_id)})
  all_recipes = mongo.db.Recipes.find()

  return render_template('edit_recipe.html', the_recipe=recipe._id, Recipes=all_recipes)

@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
  recipe_db = mongo.db.Recipes
  recipe_db.update( {'_id': ObjectId(recipe_id)},
  {
    'recipe_name': request.form.get('recipe_name'),
    'recipe_intro': request.form.get('recipe_intro'),
    'ingredients': request.form.get('ingredients'),
    'method': request.form.get('method'),
    'image': request.form.get('image')
  })
  return redirect(url_for('index', title='Updated Recipe'))

# Delete recipe file

@app.route('/delete_recipe/<recipe_id>', methods=['GET', 'POST'])
def delete_recipe(recipe_id):
  '''Delete a recipe with added confirmation'''
  recipe_db = mongo.db.Recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
  if request.method == 'GET':
    form = ConfirmDelete(data=recipe_db)
    return render_template('delete_recipe.html', title='Delete Recipe', context=recipe_db, form=form)
  form = ConfirmDelete(request.form)
  if request.method == 'POST':
    recipe_db = mongo.db.Recipes
    recipe_db.delete_one({
      '_id': ObjectId(recipe_id),
    })
    return redirect(url_for('index', condition='Welsh Recipes Updated'))
  return render_template('delete_recipe.html', title='delete recipe', recipe=recipe_db, form=form)

# Search for a recipe

@app.route('/search', methods=['POST'])
def search():
  query = request.form.get('query')
  search_recipe = mongo.db.Recipes.find({'$text': {'$search': query}})
  return render_template('search.html', search_recipe=search_recipe, query=query)

# Recipes file

@app.route('/recipes')
def recipes():
  # number of recipes per page
  per_page = 8
  """request object may have arguments (also know as parameters) if it does it gets them if not it defaults to 1 """
  page = int(request.args.get('page', 1))
  # count total number of recipes
  total = mongo.db.Recipes.count_documents({})
  # logic for what recipes to return
  all_recipes = mongo.db.Recipes.find().skip((page - 1)*per_page).limit(per_page)
  print("test = ", all_recipes)
  pages = range(1, int(math.ceil(total / per_page)) + 1)
  return render_template('recipes.html', Recipes=all_recipes, page=page, pages=pages, total=total, per_page=per_page) #info=info

@app.route('/recipe/<recipe_id>')
def recipe(recipe_id):
  '''Shows full recipe and increments view'''
  mongo.db.Recipes.find_one_and_update(
    {'_id': ObjectId(recipe_id)},
    {'$inc': {'views': 1}}
  )
  recipe_db = mongo.db.Recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
  return render_template('recipe.html', recipe=recipe_db)

@app.errorhandler(404)

def handle_404(exception):
  return render_template('404.html', exception=exception)

if __name__ == '__main__':
  # Local Host
  app.run(host='127.0.0.1', debug=True)

  # Production (Heroku)
  # app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)



