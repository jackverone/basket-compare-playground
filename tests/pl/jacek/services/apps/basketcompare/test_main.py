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
        response = self.app.post('/products/search',
                                 data=dict(name='test', info='test'),
                                 follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    # @patch('basket_compare_playground.pl.jacek.services.apps.basketcompare.main.product_controller')
    # def test_search_products_post_returns_expected_products(self, mock_product_controller):
    #     # Mock the request.form object
    #     request.form = {'name': 'test_name', 'info': 'test_info'}
    #
    #     # Mock the product_controller.search_product method
    #     mock_product_controller.search_product.return_value = [{'name': 'test_name', 'info': 'test_info'}]
    #
    #     # Call the function
    #     result = search_products_post()
    #
    #     # Assert that the function returns the expected result
    #     self.assertEqual(result, [{'name': 'test_name', 'info': 'test_info'}])
    #
    # @patch('basket_compare_playground.pl.jacek.services.apps.basketcompare.main.product_controller')
    # def test_search_products_post_returns_empty_when_no_products_found(self, mock_product_controller):
    #     # Mock the request.form object
    #     request.form = {'name': 'test_name', 'info': 'test_info'}
    #
    #     # Mock the product_controller.search_product method
    #     mock_product_controller.search_product.return_value = []
    #
    #     # Call the function
    #     result = search_products_post()
    #
    #     # Assert that the function returns an empty list when no products are found
    #     self.assertEqual(result, [])
    #
    # @patch('basket_compare_playground.pl.jacek.services.apps.basketcompare.main.product_controller')
    # def test_search_products_post_handles_missing_form_data(self, mock_product_controller):
    #     # Mock the request.form object
    #     request.form = {}
    #
    #     # Mock the product_controller.search_product method
    #     mock_product_controller.search_product.return_value = []
    #
    #     # Call the function
    #     result = search_products_post()
    #
    #     # Assert that the function handles missing form data gracefully
    #     self.assertEqual(result, [])


if __name__ == '__main__':
    unittest.main()
