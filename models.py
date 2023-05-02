"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False, unique=True)
    content = db.Column(db.String(500), nullable=False, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    rel = db.relationship('User', backref="posts")


class User(db.Model):

    __tablename__='users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    image_url=db.Column(db.Text, unique=True, nullable=True)


    def __repr__(self):
        """Show user infor"""

        
        return f"<user {self.id} {self.first_name} {self.last_name} {self.image_url}"



def connect_db(app):
    db.app = app
    db.init_app(app)