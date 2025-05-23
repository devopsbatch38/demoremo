from flask import Flask, request
import mysql.connector

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    user = request.form['username']
    password = request.form['password']

    conn = mysql.connector.connect(
        host='db',
        user='root',
        password='root',
        database='logindb'
    )

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (user, password))

    result = cursor.fetchone()

    if result:
        return "Login Successful"
    else:
        return "Invalid Credentials"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
