"""Blogly application."""

from flask import Flask, render_template, redirect, session, request
from models import db, connect_db, User


app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

with app.app_context():
    db.create_all()


@app.route('/')
def show_homepage():
    users = User.query.all()
    return render_template('home.html', users=users)

@app.route('/form')
def show_users():
    return render_template('form.html')

@app.route('/profile', methods=["POST"])
def show_profile():

    first_name = request.form['first_name']
    last_name= request.form['last_name']
    image_url= request.form['image_url']
    user = User(first_name=first_name, last_name=last_name, image_url=image_url)

    db.session.add(user)
    db.session.commit()

    return render_template('profile.html', firstname=first_name, lastname=last_name, image_url=image_url)





