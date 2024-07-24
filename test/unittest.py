import unittest
from app import app, db
from models import User

class BloglyTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
        self.client = app.test_client()

        with app.app_context():
            db.create_all()
            user = User(first_name="Test", last_name="User", image_url="https://facecard.com")
            db.session.add(user)
            db.session.commit()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_list_users(self):
        with app.app_context():
            result = self.client.get('/users')
            self.assertIn(b'Test User', result.data)

    def test_show_user(self):
        with app.app_context():
            user = User.query.first()
            result = self.client.get(f'/users/{user.id}')
            self.assertIn(b'Test User', result.data)

    def test_add_user(self):
        with app.app_context():
            result = self.client.post('/users/new', data={
                'first_name': 'New',
                'last_name': 'User',
                'image_url': 'https://facecard.com'
            }, follow_redirects=True)
            self.assertIn(b'New User', result.data)

    def test_edit_user(self):
        with app.app_context():
            user = User.query.first()
            result = self.client.post(f'/users/{user.id}/edit', data={
                'first_name': 'Edited',
                'last_name': 'User',
                'image_url': 'https://facecard.com'
            }, follow_redirects=True)
            self.assertIn(b'Edited User', result.data)

if __name__ == '__main__':
    unittest.main()
