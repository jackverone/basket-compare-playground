import logging

from basket_compare_playground.pl.jacek.services.apps.basketcompare.service.basket_service import BasketService


class BasketController:
    def __init__(self, service: BasketService):
        self.service = service

    def add_product(self, product):
        logging.info(f"add_product {product}")
        return self.service.add_product(product)

    def create_basket(self):
        return self.service.create_basket()

    def delete_basket(self, id):
        return self.service.delete_basket(id)

    def get_basket(self, id):
        return self.service.get_basket(id)
