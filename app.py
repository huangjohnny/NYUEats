import os
from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'	#not localhost since db wants 127.0.0.1 not 0.0.0.0
app.config['MYSQL_USER'] = 'ubuntu'
app.config['MYSQL_PASSWORD'] = 'cafe'
app.config['MYSQL_DB'] = 'cafeteria'
mysql = MySQL(app)
cur = mysql.connection.cursor()

#homepage
@app.route('/')
def homepage():
	return render_template('homepage.html')

#selection
@app.route('/selection')
def selection():
	return render_template('selection.html')

#menu
@app.route('/menu')
def menu():
	return render_template('menu.html')

#test connection to MySQL database
@app.route('/db')
def connect():
	cur.execute('''SHOW TABLES''')
	result = cur.fetchall()
	return str(result)
	
if __name__ == "__main__":
	app.run(debug=True)
