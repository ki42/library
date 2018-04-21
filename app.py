from flask import Flask, redirect, render_template, request, session, flash
from flask_sqlalchemy import SQLAlchemy
import cgi
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://library:lib@localhost:8889/library'
app.config['SQLALCHEMY_ECHO'] = True    

db = SQLAlchemy(app)