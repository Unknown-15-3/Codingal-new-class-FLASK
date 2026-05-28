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
    return render_template("login.html", msg= msg)    

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        mydb = mysql.connector.connect(host="remotemysql.com",
                                       user="wXy63pU5g1",
                                       password="qVOgRNMGRK",
                                       database="wXy63pU5g1")
        mycursor = mydb.cursor()
        print(username)
        mycursor.execute('SELECT * FROM LoginDetails WHERE username = %s', (username,email))
        account = mycursor.fetchone()
        print(account)
        if account:
            msg  = 'Account already exists'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers'
        elif not username or not password or not email:
            msg= 'kindly fill the details'
        else:
            mycursor.execute(
'INSERT INTO LoginDetails(username, password, email) VALUES (%s, %s, %s)',
(username, password, email)
)
            mydb.commt()
            msg = "You have register successfully"
            name = username
            return render_template('index.html', msg = msg, name=name)
    elif request.method == 'POST':
        msg = 'Kindly fill the details'
    return render_template('register.html', msg=msg)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('login.html')

app.run(host='0.0.0.0', port=8080, debug=True)