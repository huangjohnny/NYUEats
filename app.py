import os
from flask import Flask, render_template

app = Flask(__name__)

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
	
if __name__ == "__main__":
	app.run(debug=True)
