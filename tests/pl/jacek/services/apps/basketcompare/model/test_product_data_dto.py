import logging
import json

from unittest import TestCase

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_data_dto import ProductDataDto
from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.BuyBoxData import \
    BuyBoxData

from tests.pl.jacek.services.apps.basketcompare.api.external.buybox.model.buybox_json_model_examples import \
    BUYBOX_JSON_EXAMPLE_ALCHEMIK
from tests.pl.jacek.services.apps.basketcompare.api.external.buybox.model.buybox_json_model_examples import \
    BUYBOX_JSON_EXAMPLE_KARMA


class TestProductDataDto(TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        self.product_data_dto = ProductDataDto()

    def test_convert_buybox_json_alchemik_to_dto(self):
        buybox_data = BuyBoxData(json.loads(BUYBOX_JSON_EXAMPLE_ALCHEMIK))
        self.product_data_dto.convert_buybox_to_dto(buybox_data)

        self.assertIsNotNone(self.product_data_dto, "Product data should not be None")

    def test_convert_buybox_json_karma_to_dto(self):
        buybox_data = BuyBoxData(json.loads(BUYBOX_JSON_EXAMPLE_KARMA))
        self.product_data_dto.convert_buybox_to_dto(buybox_data)

        self.assertIsNotNone(self.product_data_dto, "Product data should not be None")
