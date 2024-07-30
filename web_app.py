from flask import Flask, request
import requests
import os
import signal
import json

app = Flask(__name__)

@app.route("/")
def root_path():
    return {"Hello":"Shafi"}


@app.route("/users/<string:user_id>")
def get_user(user_id):
   r = requests.get("http://127.0.0.1:5000/users/{0}".format(user_id))
   if r.status_code == 200:
        user_name = r.text.split('"')[7]
        return "<H1 id='user'>" + user_name + "</H1>"
   elif r.status_code == 404:
       return "<H1 id='error'> no such user:" + user_id + "</H1>"
   else:
       return "User not found"
   


@app.route("/stop_server")
def stopServer():
    try:
        os.kill(os.getpid(), signal.SIGINT)
        return "Sever stopped" 
    except Exception as error:
        return str(error)

if __name__ == "__main__":
    app.run(debug=True,port=5001)