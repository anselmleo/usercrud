#type: ignore
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)
userFields = {
  'id': fields.Integer,
  'fname': fields.String,
  'lname': fields.String,
  'email': fields.String
}


class UserModel(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  fname = db.Column(db.String(80), unique=False, nullable=False)
  lname = db.Column(db.String(80), unique=False, nullable=False)
  email = db.Column(db.String(80), unique=True, nullable=False)
  
  def __repr__(self):
    return f"User(fname = {self.fname}, lname = {self.lname}, email = {self.email})"
  
class Users(Resource):
  @marshal_with(userFields)
  def get(self):
    users = UserModel.query.all()
    return users
  
  @marshal_with(userFields)
  def post(self):
    args = userargs.parse_args()
    user = UserModel(fname=args["fname"], lname=args["lname"], email=args["email"])
    db.session.add(user)
    db.session.commit()
    users = UserModel.query.all()
    return users, 201
  

class User(Resource):
  @marshal_with(userFields)
  def get(self, id):
    user = UserModel.query.filter_by(id=id).first()
    if not user:
      abort(404, "User not found")
    return user



api.add_resource(Users, '/api/users/')
api.add_resource(User, '/api/users/<int:id>')

userargs = reqparse.RequestParser()
userargs.add_argument('fname', type=str, required=True, help='Firstname is required')
userargs.add_argument('lname', type=str, required=True, help='Lastname is required')
userargs.add_argument('email', type=str, required=True, help='Email is required')

@app.route("/")
def home():
  return "Hello, World!"

if __name__ == "__main__":
  app.run(port=int("3000"), debug=True)