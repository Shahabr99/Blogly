"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):

    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    image_url=db.Column(db.Text, unique=True, nullable=True)


    def __repr__(self):
        """Show user infor"""

        
        return f"<user {self.id} {self.first_name} {self.last_name} {self.image_url}"



class Tag(db.Model):

    __tablename__= "tags"

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.Text, nullable=False, unique=True)

    posts=db.relationship('Post', secondary="posts_tags", backref="tags")


class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False, unique=True)
    content = db.Column(db.String(500), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    rel = db.relationship('User', backref="posts")



class PostTag(db.Model):

    __tablename__ = "posts_tags"

    post_id=db.Column(db.Integer,db.ForeignKey('posts.id') ,primary_key=True)
    tag_id=db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)






def connect_db(app):
    db.app=app
    db.init_app(app)