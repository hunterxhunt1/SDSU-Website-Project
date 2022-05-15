# DATABASE MODELS FOR OUR USERS AND NOTES #
from . import mydb

# Module that allows our user to log in #
from flask_login import UserMixin
from sqlalchemy.sql import func

# MySQL database #
import mysql.connector

# Logs when new data is created by date and time #
# ONE TO MANY RELATIONSHIP #
class Note(mydb.Model):
	id = mydb.Column(mydb.Integer, primary_key=True)
	data = mydb.Column(mydb.String(10000))
	date = mydb.Column(mydb.DateTime(timezone=True), default=func.now())
	user_id = mydb.Column(mydb.Integer, db.ForeignKey('user.id'))



# Login Info #
class User(db.Model, UserMixin):
	id = mydb.Column(mydb.Integer, primary_key=True)
	email = mydb.Column(mydb.String(150), unique=True)
	password = mydb.Column(mydb.String(150))
	name = mydb.Column(mydb.String(150))
	notes = mydb.relationship('Note') # connects the notes and the user #