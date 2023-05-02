from unittest import TestCase
from app import app
from models import db, User

with app.app_context():
    db.drop_all()
    db.create_all()

class UserTest(TestCase):
    def setUp(self):
        """Adding a sample user"""
        User.query.delete()
        user = User(first_name='Matin', last_name = 'Basiri', image_url='https://cdn.pixabay.com/photo/2023/04/16/18/50/diabolo-7930927_960_720.jpg')
        db.session.add(matin)
        db.session.commit()
        self.user_id=user.id

    def tearDown(self):
        """reverse any changes"""
        db.session.rollback()

    def test_show_users(self):
        with app.test_client() as client:
            resp = client.get('/users')
            html = client.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
    
    def test_add_user(self):
        with app.test_client() as client:
            d = {'id': 22, 'first_name': 'Donna', 'last-name': 'Sherlington' }
            resp = client.post('/user/new', data=d)
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn(f"<a href='/user/{d.id}'>{d.first_name} {d.last_name}</a>", html)

    
    def test_change_user(self):

        with app.test_client as client:
            d = {'id': 3, 'first_name': 'Karim', 'last_name': 'Sobhuni'}
            resp = client.post(f'/users/{d.id}/edit')
            html = resp.get_data(as_text=True)
            self.assertEqual(resp.status_code, 200)
            self.assertIn(f"<a href='/user/{d.id}'>{d.first_name} {d.last_name}</a>", html)