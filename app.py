import os
import re
import math
from forms import AddRecipeForm, ConfirmDelete, EditRecipeForm
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
  four_recipes = mongo.db.Recipes.find().sort([('views', DESCENDING)]).limit(4)
  return render_template('index.html', title='Home', Recipes=four_recipes)
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
  else:
    return render_template('add_recipe.html', title='add a recipe', form=form)

@app.route('/edit_recipe/<recipe_id>', methods=['GET', 'POST'])
def edit_recipe(recipe_id):
  recipe_db = mongo.db.Recipes.find_one_or_404({'_id': ObjectId(recipe_id)})
  if request.method == 'GET':
    form = EditRecipeForm(data=recipe_db)
    return render_template('edit_recipe.html', recipe=recipe_db, form=form)
  form = EditRecipeForm(request.form)
  if request.method == 'GET':
    recipes_db = mongo.db.recipes_db
    recipes_db.update_one({
      '_id_ ObjectId(recipe_id)'
    }, {
      '$set': {
        'title': request.form['recipe_name'],
        'recipe_intro': request.form['recipe_intro'], 
        'ingredients': request.form['ingredients'],
         'method': request.form['method'],
         'image': request.form['image'],
      }
    })
    return redirect(url_for('index', title='New Recipe Added'))
  return render_template('edit_recipe.html', recipe=recipe_db, form=form)

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

'''Search for a recipe'''
@app.route('/search', methods=['POST'])
def search():
  query = request.form.get('query')
  search_recipe = mongo.db.Recipes.find({'$text': {'$search': query}})
  # using regular expression setting option for any case
  # pattern = re.compile(r"[a-zA-Z0-9\'\"\s]+")
  # print(pattern)
  # find instances of the entered word in title, tags or ingredients
  # results = mongo.db.Recipes.find({
  #   '$or': [
  #     {'recipe_name': pattern},
  #     {'ingredients': pattern},
  #   ]
  # })
  return render_template('search.html', search_recipe=search_recipe, query=query)

@app.route('/recipes')
def recipes():
  # number of recipes per page
  per_page = 8
  """You understand: so the request object may have arguments (also know as parameters) if it does it gets them if not it defaults to 1 """
  page = int(request.args.get('page', 1))
  # count total number of recipes
  total = mongo.db.Recipes.count_documents({})
  # logic for what recipes to return
  # all_recipes = mongo.db.Recipes.find().skip((page - 1)*per_page).limit(per_page)
  all_recipes = mongo.db.Recipes.find()
  print("test = ", all_recipes)
  pages = range(1, int(math.ceil(total / per_page)) + 1)
  return render_template('recipes.html', Recipes=all_recipes, page=page, pages=pages, total=total)

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



