from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""
        app.config['TESTING'] = True

    # def tearDown(self):
    #     """Stuff to do after every test."""

    def test_home_page(self):
        """Check if board is created."""
        with app.test_client() as client:
            resp = client.get('/')
            
            self.assertEqual(resp.status_code, 200)
            self.assertIn('board', session)



