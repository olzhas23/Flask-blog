from flask import Flask, render_template, request,session, flash, redirect,url_for, g

import sqlite3

DATABASE='blog.db'
USERNAME='admin'
PASSWORD='admin'
SECRET_KEY='python'


app=Flask(__name__)
app.config.from_object(__name__)

def connect_db():
	return sqlite3.connect(app.config['DATABASE.db'])
@app.route('/', methods=['GET', 'POST'])
def login():
	error=None
	if request.method == 'POST':
		if request.form ['username']!=app.config['USERNAME'] or request.form['password']!=app.config['PASSWORD']:
			error='Invalid Credentials. Please try again'
		else:
			session['logged_in']=True
		return redirect(url_for('main'))
		

	return render_template('login.html',error=error)
@app.route('/main')
@app.route('/logout')

def logout():

	session.pop('logged_in',None)  # pop method is used to reset the session key to default value
	flash('You were loged out')
	return redirect(url_for('login'))
	
def main():
	return render_template('main.html')
	

if __name__=='__main__':

	app.run(debug=True)
	

