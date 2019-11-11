import os
import re
import math
from forms import AddRecipeForm, ConfirmDelete
from config import Config
# I need to add more functionality to flask, i.e. redirect, request etc
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, DESCENDING
from pymongo import MongoClient
from bson.objectid import ObjectId
# dont think i need flash (message flashing (which is used via flask)) as the flashing system basically makes it possible to record a message at the end of a request and access it next request and only next request = usually used for remebering login and password
# Flask talking to mongo
app = Flask(__name__)

# add configuration to our flask application

app.config["MONGO_DBNAME"] = 'CookBook'
app.config["MONGO_URI"] = 'mongodb+srv://agriffiths79:motoisfun38@cluster-cookbook-1e5pm.mongodb.net/CookBook?retryWrites=true&w=majority'

# i shouldnt upload secret keys to github thus here too, but i can leave it here for now. When i come to upload this application onto the production server (heroku), its then i put it into environment variables inside heroku itself 
app.config['SECRET_KEY'] = 'nwoiefdjowijefoiwjefoiwefjowiefj'

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
  four_recipes = mongo.db.Recipes.find()#.sort([('views', DESCENDING)]).limit(1)
  return render_template('index.html', title='Home', recipes=four_recipes)
  # below is a setting stone to if my production site works
  # return 'Hello'

@app.route('/add_recipe', methods=['GET', 'POST']) #routing identifier will have the same name as the function name (its a choice as its easier for a beginner)
def add_recipe():
  """Creates a recipe and enters into recipe collection"""
  form = AddRecipeForm(request.form)
  # if form.validate_on_submit(): THIS 1 DOESNT WORK. WHY?
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
  return render_template('add_recipe.html', title='add a recipe', form=form)



@app.route('/delete_recipe/<recipe_id>', methods=['GET', 'POST'])
def delete_recipe(recipe_id):
  '''Delete a recipe with added confirmation'''
  recipe_db = mongo.db.Recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
  if request.method == 'GET':
    form = ConfirmDelete(data=recipe_db)
    return render_template('delete_recipe.html', title='Delete Recipe', form=form)
  form = ConfirmDelete(request.form)
  if request.method == 'GET':
    recipe_db = mongo.db.Recipes
    recipe_db.delete_one({
      '_id': ObjectId(recipe_id),
    })
    return redirect(url_for('index', title='Welsh Recipes Updated'))
  return render_template('delete_recipe.html', title='delete recipe', recipe=recipe_db, form=form)

@app.route('/search')
def search():
  '''Search for a recipe'''
  search_recipe = request.args['pattern']
  # using regular expression setting option for any case
  pattern = re.compile(r"[a-zA-Z0-9]+")
  # find instances of the entered word in title, tags or ingredients
  results = mongo.db.recipes.find({
    '$or': [
      {'title': pattern},
      {'tags': pattern},
      {'ingredients': pattern}
    ]
  })
  return render_template('search.html', pattern=search_recipe, results=results)

  


if __name__ == '__main__':
  # Local Host
  app.run(host='127.0.0.1', debug=True)

  # Production (Heroku)
  # app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)