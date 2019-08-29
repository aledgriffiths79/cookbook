import os
from flask import Flask
#Flask talking to mongo
app = Flask(__name__)

@app.route('/')
def hello():
  return 'Hello World whats news'

if __name__ == '__main__':
  # Local Host
  app.run(host='127.0.0.1', debug=True)

  # Production (Heroku)
  # app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)