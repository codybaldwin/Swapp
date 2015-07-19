from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'John'}
	return render_template('index.html', user = user)

@app.route('/login')
def login():
	return render_template('login.html')