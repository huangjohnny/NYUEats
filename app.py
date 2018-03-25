import os, time
from flask import Flask, render_template, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = '127.0.0.1'	#not localhost since db wants 127.0.0.1 not 0.0.0.0
app.config['MYSQL_USER'] = 'ubuntu'
app.config['MYSQL_PASSWORD'] = 'cafe'
app.config['MYSQL_DB'] = 'cafeteria'
mysql = MySQL(app)
#mysql.connection.autocommit(True)
cur = mysql.connection.cursor()

app.secret_key = os.urandom(24)


#homepage
@app.route('/')
def homepage():
	#a session variable will act as a cart, a python list holding all orders
	session['orders'] = []		
	return render_template('homepage.html')

#selection
@app.route('/selection')
def selection():
	return render_template('selection.html')

#menu
@app.route('/menu')
def menu():
	return render_template('menu.html')

@app.route('/detail')
def detail():
	return render_template('detail.html')

@app.route('/checkout')
def checkout():
	return render_template('checkout.html')

@app.route('/pickuptime')
def pickuptime():
	return render_template('pickuptime.html')

#test connection to MySQL database
@app.route('/db')
def connect():
	cur.execute('''SHOW TABLES''')
	result = cur.fetchall()
	return str(result)

#test creating a order with a nyu id
#@app.route('/create/order')
#def order():
	#get nyu id from html form and create table with the same name
	#netid = 
	#cur.execute('''CREATE TABLE %s (name VARCHAR(20) NOT NULL, time TIME)''', netid)
	#get pickup time from html form and insert to table
	#pickuptime = time.strptime(       , '%Y-%m-%d %H:%M:%S')
	#pickuptime = time.strftime('%Y-%m-%d %H:%M:%S', pickuptime)
	#cur.execute('''INSERT INTO %s (time) VALUES (%s)''', (netid, pickuptime))
	#insert orders into table
	#for item in session['orders']:
		#cur.execute('''INSERT INTO %s (name) VALUES (%s)''', (netid, item))
	#clear the cart
	#session.pop('orders')
	#commit at the very end


if __name__ == "__main__":
	app.run(debug=True)
