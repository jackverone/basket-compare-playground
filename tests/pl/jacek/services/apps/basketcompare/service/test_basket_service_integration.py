import logging
import json

from unittest import TestCase

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.BuyBoxData import \
    BuyBoxData
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_data_dto import ProductDataDto

from basket_compare_playground.pl.jacek.services.apps.basketcompare.repository.basket_repository import BasketRepository
from basket_compare_playground.pl.jacek.services.apps.basketcompare.service.basket_service import BasketService
from basket_compare_playground.pl.jacek.services.apps.basketcompare.repository.ProductRepository import \
    ProductRepository
from basket_compare_playground.pl.jacek.services.apps.basketcompare.service.product_service import ProductService

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.service.BuyBoxService import \
    BuyBoxService
from tests.pl.jacek.services.apps.basketcompare.api.external.buybox.model.buybox_json_model_examples import \
    BUYBOX_JSON_EXAMPLE_ALCHEMIK, BUYBOX_JSON_EXAMPLE_KARMA


class TestIntegrationBasketService(TestCase):

    def __init__(self, methodName: str = "runTest"):
        super().__init__(methodName)

    def setUp(self):
        logging.basicConfig(
            level=logging.INFO,
            format='[%(asctime)s] %(levelname)s in %(filename)s %(module)s %(funcName)s: %(message)s'
        )

        self.product_data_dto_alchemik = ProductDataDto()
        self.product_data_dto_karma = ProductDataDto()
        self.product_data_dto_bambuko = ProductDataDto()

        self.product_service = ProductService(ProductRepository(), BuyBoxService())
        self.basket_service = BasketService(BasketRepository())

    def test_create_basket_compare(self):
        with (open("pl/jacek/services/apps/basketcompare/api/external/buybox/model/buybox_example_alchemik.json")
              as file_json_data_alchemik):
            # smaller amount of test data
            # buybox_data_alchemik = BuyBoxData(json.loads(BUYBOX_JSON_EXAMPLE_ALCHEMIK))

            # full amount of test data
            buybox_data_alchemik = BuyBoxData(json.load(file_json_data_alchemik))
            self.product_data_dto_alchemik.convert_buybox_to_dto(buybox_data_alchemik)

        with (open("pl/jacek/services/apps/basketcompare/api/external/buybox/model/buybox_example_karma.json")
              as file_json_data_karma):
            # smaller amount of test data
            # buybox_data_karma = BuyBoxData(json.loads(BUYBOX_JSON_EXAMPLE_KARMA))

            # full amount of test data
            buybox_data_karma = BuyBoxData(json.load(file_json_data_karma))
            self.product_data_dto_karma.convert_buybox_to_dto(buybox_data_karma)

        with (open("pl/jacek/services/apps/basketcompare/api/external/buybox/model/buybox_example_bambuko.json")
              as file_json_data_bambuko):
            # smaller amount of test data
            # buybox_data_bambuko = BuyBoxData(json.loads(BUYBOX_JSON_EXAMPLE_BAMBUKO))

            # full amount of test data
            buybox_data_bambuko = BuyBoxData(json.load(file_json_data_bambuko))
            self.product_data_dto_bambuko.convert_buybox_to_dto(buybox_data_bambuko)

        self.basket_service.add_product(self.product_data_dto_alchemik)
        # self.basket_service.add_product(self.product_data_dto_karma)
        self.basket_service.add_product(self.product_data_dto_bambuko)

        all_products = self.basket_service.get_all_products()
        # logging.info(f"all_products={all_products}")

        basket_compare = self.basket_service.create_basket_compare(all_products)
        # logging.info(f"basket_compare={basket_compare}")
        # for k, v in basket_compare.items():
        #     logging.info(f"create_basket_compare: len={len(v)}, k={k}, v={v} \n")
        #     for product in v:
        #         logging.info(f"create_basket_compare: product={product} \n")

        # self.basket_service.add_product()
        # self.fail()
