# THIS IS GOING TO STORE THE ROUTES THAT THE USER WILL GO TO #
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
	return render_template("First Page.html")