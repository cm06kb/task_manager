from flask import Flask
from flask_restful import Api, Resource, Reqparse 

app = Flask(__name__)
api = Api(app)

users = [{"name": "Bill", "age": "15",
          "occupation": "teacher"}, {"name": "Bob", 
          "age": "25",
          "occupation": "nurse"},{"name": "Jenny", 
          "age": "75",
          "occupation": "doctor"]]

Class User(Resource):
    def get(self, name):
        for user in users:
            if(name==user["name"]):
                return user, 200
        return "user not found", 404
            
    def post(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
        
        for user in users:
            if(name==user["name"]):
                return "user with name () already exists".fornat("name"), 400
        user = {"name": name, "age":args["age"], "occupation": args["occupation"]}
        users.append(user)
        return user, 201
    
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument("age")
        parser.add_argument("occupation")
        args = parser.parse_args()
        
        for user in users:
            if(name==user["name"]):
                user["age"] = args["age"]
                user["occupation"] = args["occupation"]
                return user, 200
                
                
        
        user = {"name": name, "age":args["age"], "occupation": args["occupation"]}
        users.append(user)
        return user, 201
        
    def delete(self, name):
        global users
        users = [user for user in users if user["name"] != name]
        return "{} is deleted.".format(name), 200
    