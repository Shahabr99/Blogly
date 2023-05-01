from unittest import TestCase
from app import app
from models import db, User

db.drop_all()
db.create_all()

class TestUser(TestCase):
    def setUp(self):
        """Clean up existing table"""
        User.query.delete()

    def tearDown(self):
        """Clean up any fouled transaction"""
        db.session.rollback()   

    