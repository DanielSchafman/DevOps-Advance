from flask import Flask
import requests


app = Flask(__name__)

@app.route("/")
def root_path():
    return {"Hello":"Shafi"}


@app.route("/users/<int:user_id>")
def get_user(user_id):
    r = requests.get("http://127.0.0.1:5000/users/{0}".format(user_id))
    return r.text


if __name__ == "__main__":
    app.run(debug=True,port=5001)