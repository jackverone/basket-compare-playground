import unittest
from unittest.mock import patch, Mock
from flask import request
from basket_compare_playground.pl.jacek.services.apps.basketcompare.main import app

from basket_compare_playground.pl.jacek.services.apps.basketcompare.main import search_products_post
from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.constants import SELECTED_PRODUCTS_SESSION_KEY


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_search_product_view(self):
        response = self.app.get('/products/search', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_search_product_post(self):

        self.app.get('/', follow_redirects=True)

        # self.app.post('/products/search',
        #                          data=dict(name='Karma', info='Sadhguru'),
        #                          follow_redirects=True)

        self.app.post('/products/add',
                      data=dict(name='Alchemik', info='Paulo Coelho'),
                      follow_redirects=True)

        self.app.post('/products/add',
                      data=dict(name='Bambuko', info='Nosowska'),
                      follow_redirects=True)

        response = self.app.get('/basket_compare', follow_redirects=True)

        # self.assertEqual(response.status_code, 200)
        # self.assertNotEqual(self.app.session[SELECTED_PRODUCTS_SESSION_KEY], {}, 'Session should not be empty')
        # self.assertEqual(self.app.session[SELECTED_PRODUCTS_SESSION_KEY]['test'], 'test')


if __name__ == '__main__':
    unittest.main()
