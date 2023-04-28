"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)


class User(db.Model):

    __tablename__='users'

    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    image_url=db.Column(db.Text, unique=True, nullable=True)


    def __repr__(self):
        """Show user infor"""

        p=self
        return f"<user {p.id} {p.first_name} {p.last_name} {p.image_url}"