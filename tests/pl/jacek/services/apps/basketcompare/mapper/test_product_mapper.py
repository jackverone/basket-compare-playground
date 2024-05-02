import logging
from unittest import TestCase

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product import Product
from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.Datum import Datum
from basket_compare_playground.pl.jacek.services.apps.basketcompare.mapper.product_mapper import from_datum


class Test(TestCase):

    def setUp(self):
        logging.basicConfig(
            level=logging.INFO,
            format="[%(asctime)s] %(levelname)s in %(filename)s %(module)s %(funcName)s: %(message)s"
        )

    def test_from_datum(self):
        # Given
        datum_data = {
            "id": 193153244,
            "name": "Legimi",
            "product_name": "Alchemik",
            "icon": "https://assets.buybox.click/5d826a78650f0ec8eca2900d28035ea605514be3.png",
            "logo": "https://assets.buybox.click/6b6f67f35b5e1c138dd2ad2bd7032fda9528f2c5.png",
            "type": "audiobook",
            "typeId": 3,
            "typeName": "audiobook",
            "shopId": 9,
            "currency": "PLN",
            "price": "14.99",
            "pricePrefix": "od"
        }
        datum = Datum(datum_data)
        datum_dict = datum.to_dict()

        # When
        product: Product = from_datum(datum)
        product_dict = product.to_dict()

        # Then
        self.assertEqual(datum_dict, product_dict)
