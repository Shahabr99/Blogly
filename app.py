"""Blogly application."""

from flask import Flask, render_template, redirect, session, request
from models import db, connect_db, User
from models import Post

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
    posts = Post.query.filter(Post.user_id == id).all()
    return render_template('profile.html', user=user, posts=posts)


@app.route('/users/<int:id>/edit')
def edit_user(id):

    user_info = User.query.get_or_404(id)

    return render_template('edit.html', user=user_info)


@app.route('/users/<int:id>/edit', methods=['POST'])
def change_user(id):
    """Changing info of a user"""

    target_user = User.query.get(id)
    name = request.form['fname']
    lastname = request.form['lname']
    image = request.form['img_url']

    target_user.first_name = name
    target_user.last_name = lastname
    target_user.image_url = image

   
    db.session.add(target_user)
    db.session.commit()
    
    users = User.query.all()

    return render_template('users.html', users = users)


@app.route('/users/<int:id>/delete')
def delete_user(id):
    """Delete a user"""
    user = User.query.get(id)

    db.session.delete(user)
    db.session.commit()

    users = User.query.all()
    return render_template('users.html', users=users)


@app.route('/users/<int:id>/posts/new')
def post_form(id):
    """Loads the form and user can post"""
    return render_template('post.html', id=id)


@app.route('/users/<int:id>/posts/new', methods=["POST"])
def show_posts(id):
    title = request.form['title']
    content = request.form['content']

    post = Post(title = title, content=content, user_id=id)

    db.session.add(post)
    db.session.commit()


    return redirect(f"/user/{id}")


@app.route('/posts/<int:id>')
def post_details(id):
    post = Post.query.get(id)
    return render_template('post_content.html', post=post)


@app.route('/cancel/<int:id>')
def cancelled(id):

    return redirect(f'/user/{id}')


@app.route('/delete/<int:id>')
def delete_post(id):
    post = Post.query.get(id)
    id = post.user_id
    
    db.session.delete(target_post)
    db.session.commit()

    return redirect(f'/user/{id}')


@app.route('/edit/<int:id>')
def edit_post(id):
    post=Post.query.get(id)
    return render_template('edit_post.html', post=post)


@app.route('posts/<int:id>/edit', methods=['POST'])
def post_edition(id):
    title = request.form['title']
    content = request.form['content']

    