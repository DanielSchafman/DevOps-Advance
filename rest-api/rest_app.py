from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import database.creds as creds
import CurrentTime
import os
import signal


app = Flask(__name__)

# Configuration
app.config['MYSQL_HOST'] = creds.MYSQLHOST
app.config['MYSQL_USER'] = creds.DBUSERNAME
app.config['MYSQL_PASSWORD'] = creds.DBPASS
app.config['MYSQL_DB'] = creds.MYSQLDB

mysql = MySQL(app)

# Building the endpoints

#POST
@app.route('/users/<int:user_id>', methods=['POST'])
def add_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "reason": "Invalid input"}), 400

    user_name = data.get('user_name')
    if not user_name:
        return jsonify({"status": "error", "reason": "Missing user_name"}), 400

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
    user = cursor.fetchone()

    if user:
        return jsonify({"status": "error", "reason": "id already exists"}), 500

    creation_date = CurrentTime.CurrentTime._get_current_time()
    cursor.execute('INSERT INTO users (id, user_name, creation_date) VALUES (%s, %s, %s)', 
                   (user_id, user_name, creation_date))
    mysql.connection.commit()
    cursor.close()

    return jsonify({"status": "ok", "user_added": user_name}), 200

#GET
@app.route('/users/<int:user_id>',methods=['GET'])
def get_user(user_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT user_name FROM users WHERE id = %s', (user_id,))
    user = cursor.fetchone()
    cursor.close()

    if user:
        return jsonify({"status": "ok", "user_name": user['user_name']}), 200
    else:
        return jsonify({"status": "error", "reason": "no such id"}), 500

#PUT
@app.route('/users/<int:user_id>',methods=['PUT'])
def change_user(user_id):
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "reason": "Invalid input"}), 400

    user_name = data.get('user_name')
    if not user_name:
        return jsonify({"status": "error", "reason": "Missing user_name"}), 400

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
    user = cursor.fetchone()

    if not user:
        return jsonify({"status": "error", "reason": "no such id"}), 500

    cursor.execute('UPDATE users SET user_name = %s WHERE id = %s', (user_name, user_id))
    mysql.connection.commit()
    cursor.close()

    return jsonify({"status": "ok", "user_updated": user_name}), 200


#DELETE
@app.route('/users/<int:user_id>',methods=['DELETE'])
def delete_user(user_id):
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
    user = cursor.fetchone()

    if not user:
        return jsonify({"status": "error", "reason": "no such id"}), 500

    cursor.execute('DELETE FROM users WHERE id = %s', (user_id,))
    mysql.connection.commit()
    cursor.close()

    return jsonify({"status": "ok", "user_deleted": user_id}), 200


#stopping the server
@app.route("/stop_server")
def stop_server():
    try:
        os.kill(os.getpid(), signal.SIGINT)
        return "Server stopped"
    except Exception as error:
        return str(error)


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
