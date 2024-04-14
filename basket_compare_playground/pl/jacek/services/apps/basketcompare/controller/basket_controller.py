import logging
from typing import List

from basket_compare_playground.pl.jacek.services.apps.basketcompare.service.basket_service import BasketService
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_data_dto import ProductDataDto


class BasketController:
    def __init__(self, service: BasketService):
        self.service = service

    def get_all_products(self):
        logging.info(f"get_all_products()")
        return self.service.get_all_products()

    def add_product(self, product):
        logging.info(f"add_product {product}")
        return self.service.add_product(product)

    def create_basket_compare(self, products: List[ProductDataDto]):
        logging.info(f"create_basket_compare({products})")
        return self.service.create_basket_compare(products)
