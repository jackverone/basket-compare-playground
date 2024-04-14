import logging

from basket_compare_playground.pl.jacek.services.apps.basketcompare.service.basket_service import BasketService


class BasketController:
    def __init__(self, service: BasketService):
        self.service = service

    def get_all_products(self):
        logging.info(f"get_all_products()")
        return self.service.get_all_products()

    def add_product(self, product):
        logging.info(f"add_product {product}")
        return self.service.add_product(product)
