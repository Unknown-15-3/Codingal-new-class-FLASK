from flask import Flask, render_template, request
import mysql.connector
import re

app = Flask(__name__)

@app.route('/login', methods=['GET','POST'])
def login():
    msg= ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        mybd = mysql.connector.connect(host="remotemysql.com",
user="wXy63pU5g1",
password="qVOgRNMGRK",
database="wXy63pU5g1"
        )
        mycursor = mybd.cursor()
        mycursor.execute(
            'SELECT * FROM LoginDetails WHERE username = %s AND password = %s',
            (username, password)
        )
        account = mycursor.fetchone()
        if account:
            print('login successful')
            name= account[1]
            id = account[0]
            msg= 'Login successful'
            print('login is successful')
            return render_template('welcome.html', msg=msg, name=name, id=id)
        else:
            msg= 'invalid credentials. Kindly check'
            return render_template('login.html', msg=msg)
    else:
        return render_template('login.html', msg=msg)
    
@app.route("/logout")
def logout():
    name= ''
    id= ''
    msg = "Logout successfully"
    return render_template("login.html", msg= msg, name=name, id=id)    