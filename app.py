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
    return redirect('/users')

@app.route('/users')
def show_users():
        users = User.query.all()
        return render_template('users.html', users=users)

@app.route('/user/new')
def load_form():
    return render_template('form.html') 


@app.route('/user/new', methods=["POST"])
def add_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    image_url = request.form['image_url']

    new_user = User(first_name = first_name, last_name=last_name, image_url = image_url)

    db.session.add(new_user)
    db.session.commit()

    users = User.query.all()

    return render_template('users.html', users=users)

@app.route('/user/<int:id>')
def show_user(id):
    user = User.query.get_or_404(id)
    
    return render_template('profile.html', user=user)