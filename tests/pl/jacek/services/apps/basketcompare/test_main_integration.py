import unittest
from unittest.mock import patch, Mock
from flask import request
from basket_compare_playground.pl.jacek.services.apps.basketcompare.main import app

from basket_compare_playground.pl.jacek.services.apps.basketcompare.main import search_products_post


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_search_product_view(self):
        response = self.app.get('/products/search', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_search_product_post(self):
        self.app.get('/', follow_redirects=True)

        response = self.app.post('/products/search',
                                 data=dict(name='Karma', info='Sadhguru'),
                                 follow_redirects=True)

        self.app.post('/products/add',
                      data=dict(name='Karma', info='Sadhguru'),
                      follow_redirects=True)

        self.app.get('/basket_compares', follow_redirects=True)

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
