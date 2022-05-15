# render_template --> Renders the html template
# request 		  --> Get info that's sent to form
# flash			  --> Flash a message to user 

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User

# Secure password by hashing it #
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET','POST'])
def login():
	if request.method == 'POST' and 'email' in requesnt.form and 'name' in request.form and 'password1' in request.form:
		email = request.form['email']
		name = request.form['name']
		password1 = request.form['password1']

		if len(email) < 4:
			flash('Invalid Email!', category='error')
		elif len(name) < 2:
			flash('Name must be more than 2 characters', category='error')
		elif password1 != password2:
			flash("Passwords doesn't match!", category='error')
		elif len(password1) < 8:
			flash('Password must be greater than 8 characters', category='error')
		else:
			# PUT TO DATABASE #	
			new_user = User(email=email, name=name, password=generate_password_hash(password1, method="sha256"))
			mydb.session.add(new_user)
			mydb.session.commit()
			flash('Thank you for signing up!', category='success')
			return redirect(url_for('views.home'))

	return render_template("Login.html")
