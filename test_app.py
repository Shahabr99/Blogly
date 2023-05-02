from unittest import TestCase
from app import app
from models import db, User


db.drop_all()
db.create_all()

class UserTest(TestCase):
    def setUp(self):
        """Adding a sample user"""
        User.query.delete()
        matin = User(first_name='Matin', last_name = 'Basiri', image_url='https://cdn.pixabay.com/photo/2023/04/16/18/50/diabolo-7930927_960_720.jpg')
        db.session.add(matin)
        db.session.commit()

    def tearDown(self):
        """reverse any changes"""
        db.session.rollback()

    def test_show_users(self):
        with app.test_client() as client:
            resp = client.get('/users')
            self.assertEqual(resp.status_code, 200)
    
    def test_add_user(self):
        with app.test_client() as client:
            d = {'first_name': 'Donna', 'last-name': 'Sherlington', 'image_url':'https://cdn.pixabay.com/photo/2016/03/23/04/01/woman-1274056_960_720.jpg' }
            resp = client.post('/user/new', data=d)
            # html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            # self.assertIn(f'<a href="/user/user.id">d.first_name d.last_name</a></li>', html)

    def test_