import os
# I need to add more functionality to flask, i.e. redirect, request etc
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, DESCENDING
from bson.objectid import ObjectId

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

@app.route('/add_recipe') #routing identifier will have the same name as the function name (its a choice as its easier for a beginner)
def add_recipe():
  return render_template('add_recipe.html')

if __name__ == '__main__':
  # Local Host
  app.run(host='127.0.0.1', debug=True)

  # Production (Heroku)
  # app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)