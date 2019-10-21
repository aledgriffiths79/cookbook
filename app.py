import os
import re
import math
from forms import AddRecipeForm
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
  if form.validate_on_submit():
    # set the collection
    recipes_db = mongo.db.Recipes
    # insert the new recipe
    recipes_db.insert_one({
      'recipe_name': request.form['recipe_name'],
      'recipe_intro': request.form['recipe_intro'],
      'ingredients': request.form['ingredients'],
      'image': request.form['image'],
      'views': 0

    })
    return redirect(url_for('index', title='New Recipe Added'))
  return render_template('add_recipe.html')

if __name__ == '__main__':
  # Local Host
  app.run(host='127.0.0.1', debug=True)

  # Production (Heroku)
  # app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)