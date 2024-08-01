#type: ignore
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class UserModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  fname = db.Column(db.String(80), unique=False, nullable=False)
  lname = db.Column(db.String(80), unique=False, nullable=False)
  email = db.Column(db.String(80), unique=True, nullable=False)
  
  def __repr__(self):
    return f"User(fname = {self.fname}, lname = {self.lname}, email = {self.email})"

@app.route("/")
def home():
  return "Hello, World!"

if __name__ == "__main__":
  app.run(port=int("3000"), debug=True)