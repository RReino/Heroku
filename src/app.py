from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__, template_folder='templates')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)


@app.route('/')
def index():
    a = "y"
    if a == "y":
        return redirect(url_for('form'))


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return "Login via the login Form"

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''', (name, age))
        mysql.connection.commit()
        cursor.close()
        return f"LOL!"


app.run(host='localhost', port=5000, debug=True)