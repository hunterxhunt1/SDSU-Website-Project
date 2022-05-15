from flask import Flask, render_template, request, flash, url_for, redirect, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
from datetime import timedelta
import mysql.connector
import re


app = Flask(__name__)

# Creates a secret key for website protection #
app.secret_key = 'This is the secret key'

# Set time for how long a user-session is #
app.permanent_session_lifetime = timedelta(minutes=5)

# Establish MySQL connection #
mydb = mysql.connector.connect(host="localhost", user ="root", passwd="1234", database="mydb")

# Establish cursor to navigate database #
cursor = mydb.cursor()

## LOGIN ROUTE ##
@app.route('/login/', methods = ["GET","POST"])
def login():

	# Sign-Up checker #
	if request.method == 'POST' and 'email' in request.form and 'name' in request.form and 'password1' in request.form:
		email = request.form['email']
		name = request.form['name']
		password1 = request.form['password1']

		if email == '' and name == '' and password1 == '':
			flash('Invalid. Please Try Again!', category="error")
		elif email == '':
			flash('Enter a valid Email!', category='error')
		elif name =='':
			flash('Enter a valid Name', category='error')
		elif password1 == '':
			flash('Please enter password!')

		else:
			cursor.execute('INSERT INTO user (name, password, email) VALUES (%s,%s,%s)', (name,password1,email))
			mydb.commit()
			flash('Sign-Up Complete! Please Login.', category="success")

		return render_template("Login.html")

	# Login cheker #
	elif request.method == 'POST' and 'email' in request.form and 'password' in request.form:
		email = request.form['email']
		password = request.form['password']


		if email == '':
			flash('Invalid! Enter Email.', category='error')
		elif password == '':
			flash('Invalid! Enter Password.', category='error')

		else:

			# Establish 'session' --> Logs the same user until logout #
			session.permanent = True
			session['email'] = email			

			# See if account exist #
			cursor.execute("""SELECT * FROM user WHERE email = %s AND password = %s""", (email,password,))
			check = cursor.fetchall()

			if check:			
				if "email" in session:					
					return redirect(url_for("home"))

			else:
				flash('Incorrect Email or Password! Try Again.', category="error") 
				return render_template("Login.html")

	return render_template('Login.html')
## END LOGIN ##

@app.route("/logout")
def logout():
	session.pop("email", None)
	flash('Thank you for visiting!', category="success")
	return redirect(url_for("login"))


## HOME PAGE ##
@app.route("/home")
def home():
	if "email" in session:
		email = session["email"]
		return render_template("First Page.html")
	else:
		flash("Login or Sign-Up!", category="error")
		return redirect(url_for("login"))

	return render_template("First Page.html")
## END HOME PAGE ##


## EVENTS PAGE ##
@app.route("/events")
def events():
	if "email" in session:
		email = session["email"]
		return render_template("Events.html")

	else:
		flash("Login or Sign-Up!", category="error")
		return redirect(url_for("login"))



	return render_template("Events.html")

## END EVENTS ##


## STORE PAGE ##
@app.route("/store", methods = ["GET","POST"])
def store():
	if "email" in session:
		email = session["email"]

		if request.method == "POST" and 'fname' in request.form and 'lname' in request.form and 'address' in request.form and 'city' in request.form and 'state' in request.form and 'zip' in request.form and 'phone' in request.form and 'email' in request.form and 'card' in request.form and 'cvv' in request.form and 'date' in request.form:
			fname = request.form["fname"]
			lname = request.form["lname"]
			address = request.form["address"]
			city = request.form["city"]
			state = request.form["state"]
			zipcode = request.form["zip"]
			phone = request.form["phone"]
			email1 = request.form["email"]
			card = request.form["card"]
			cvv = request.form["cvv"]
			dates = request.form["date"]

			if fname == '' or lname == '' or address == '' or city == '' or state == '' or zipcode == '' or phone == '' or email1 == '' or card == '' or cvv == '' or dates == '' :
				flash("Please Fill Everything Out", category = "error")

			else:
				cursor.execute(""" INSERT INTO cardinfo (first,last,address,city,state,zip,phone,email,card,cvv,dates) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) """, (fname,lname,address,city,state,zipcode,phone,email1,card,cvv,dates))	
				mydb.commit()

		return render_template("Store.html")
		
	
	else:
		flash("Login or Sign-Up!", category="error")
		return redirect(url_for("login"))

	return render_template("Store.html")

## END STORE ##

## ABOUT PAGE ##
@app.route("/about")
def about():
	if "email" in session:
		email = session["email"]
		return render_template("About_Us.html")
	else:
		flash("Login or Sign-Up!", category="error")
		return redirect(url_for("login"))	

	return render_template("About_Us.html")
## END CART ##


## CART PAGE ##
@app.route("/cart")
def cart():
	if "email" in session:
		email = session["email"]
		return render_template("Cart.html")
	else:
		flash("Login or Sign-Up!", category="error")
		return redirect(url_for("login"))

	return render_template("Cart.html")
## END CART ##

@app.route("/registration", methods = ["GET", "POST"])
def registration():
	if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'phone' in request.form and 'people' in request.form and 'event' in request.form:

		name = request.form['name']
		email = request.form['email']
		phone = request.form['phone']
		people = request.form['people']
		event = request.form['event']

		if name == '':
			flash("Enter a valid NAME!", category = "error")
		elif email == '':
			flash("Enter a valid EMAIL!", category ="error")
		elif phone == '':
			flash("Enter a valid PHONE NUMBER!", category ="error")			
		elif people == '':
			flash("PEOPLE field is empty", category ="error")
		else:
			cursor.execute("""INSERT INTO registration (name, email, phone,people,event) VALUES (%s,%s,%s,%s,%s)""", (name,email,phone,people,event))
			mydb.commit()

			flash('Registration Complete!', category="success")

	return render_template("Registration.html")


if __name__ =='__main__':
	app.run(debug = True)