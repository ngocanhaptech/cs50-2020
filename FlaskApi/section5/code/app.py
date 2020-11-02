from flask import Flask
from flask_restful import Api
from flask_jwt import JWT # JWT : lib
from security import authenticate, identity # JWT : function
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
app.secret_key = "jose" # JWT: key 
api = Api(app)

jwt = JWT(app, authenticate, identity) # JWT: jwt object #/auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

app.run(port=5000, debug=True)