from flask import Flask, request, jsonify

app = Flask(__name__)

data_dict = {}


@app.route("/create", methods=["POST"])
def create():
    if request.method == "POST":
        new_entry = request.get_json()
        data_dict[new_entry.get("id")] = new_entry
        return "created succesfully"


@app.route("/get")
def get():
    return data_dict


@app.route("/update/<int:id>", methods=["PUT"])
def update(id):
    if request.method == "PUT":
        updated_entry = request.get_json()
        data_dict[id] = updated_entry
        return "entry updated succesfully"


@app.route("/delete/<int:id>", methods=["DELETE"])
def delete(id):
    if request.method == "DELETE":
        del data_dict[id]
        return f"deleted {id} entry succesfully "


if __name__ == "__main__":
    app.run()
