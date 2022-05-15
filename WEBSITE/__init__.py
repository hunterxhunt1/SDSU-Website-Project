from flask import Flask
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from os import path
import mysql.connector


mydb = MySQL()

def create_app():
	app = Flask(__name__)

	# Encrypt/Protect our cookies or session data on our website and initializing app #
	app.secret_key = 'This is the secret key'

	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:1234@localhost/mydb'
	# app.config['MYSQL_HOST'] = mydb['localhost']
	# app.config['MYSQL_USER'] = mydb['root']
	# app.config['MYSQL_PASSWORD'] = mydb['1234']
	# app.config['MYSQL_DB'] = mydb['mydb']


	# MYSQL Connection #
	# mydb = mysql.connector.connect(host="localhost", user ="root", passwd="1234", database="mydb")
	mydb.init_app(app)

	# connect the file 'views' and 'auth' to this file #
	from .views import views
	from .auth import auth

	# No Prefix #
	app.register_blueprint(views, url_prefix='/')
	app.register_blueprint(auth, url_prefix='/')

	from .models import User, Note

	create_database(app)


	return app


def create_database(app):
	if not path.exists('WEBSITE/' + 'mydb'):
		mydb.create_all(app=app)
		print('Created Database!')
