from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors
import creds
import CurrentTime

app = Flask(__name__)

# Configuration
app.config['MYSQL_HOST'] = creds.MYSQLHOST
app.config['MYSQL_USER'] = creds.DBUSERNAME
app.config['MYSQL_PASSWORD'] = creds.DBPASS
app.config['MYSQL_DB'] = creds.MYSQLDB

mysql = MySQL(app)

# Building the endpoints
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

if __name__ == '__main__':
    app.run(debug=True)