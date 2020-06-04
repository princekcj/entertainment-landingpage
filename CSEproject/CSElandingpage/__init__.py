
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='landingtemplates')
app.config['SECRET_KEY'] = '3691628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cseemails.db'
db = SQLAlchemy(app)

from CSElandingpage import routes