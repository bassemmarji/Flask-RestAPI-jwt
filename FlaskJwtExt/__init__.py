import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

#Defining a Flask Application
app = Flask(__name__)
#Initialize the API
api = Api(app)

#Application Configuration
basedir = os.path.abspath( os.path.dirname(__file__))
database_path = "sqlite:///{}".format(os.path.join(basedir,"db", "dblibrary.db"))

app.config['SQLALCHEMY_DATABASE_URI'] = database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'My Secret Key'
app.config['JWT_SECRET_KEY'] = 'My Secret Key'

app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access','refresh']

db = SQLAlchemy(app)
#Adding JSON Web Tokenization to our application
jwt = JWTManager(app)



