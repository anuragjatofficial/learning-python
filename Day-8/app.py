from flask import Flask, request, jsonify
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient(
    "mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.0.2"
)


db = client["mydb"]


class User:
    def __init__(self, name, passowrd, email):
        self.name = name
        self.password = passowrd
        self.email = email


@app.route("/users", methods=["POST", "GET"])
def addOrGet():
    if request.method == "POST":
        user_data = request.get_json()
        username = user_data["username"]
        password = user_data["password"]
        email = user_data["email"]
        user = User(username, password, email)
        result = db.users.insert_one(user.__dict__)
        inserted_user = db.users.find_one({'_id':result.inserted_id})
        inserted_user['_id'] = str(inserted_user['_id'])
        return jsonify(inserted_user)
    else:
        res = db.users.find()
        users_list = [user for user in res]
        for user in users_list:
            user['_id'] = str(user['_id'])
        return jsonify(users_list)


if __name__ == "__main__":
    app.run()
