import logging
from typing import List

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.basket import Basket
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_data_dto import ProductDataDto


class BasketRepository:
    def __init__(self):
        self.baskets = []
        self.products = []  # type: List[ProductDataDto]

    def get_all_products(self):
        logging.info(f"get_all_products() = {self.products}")
        return self.products

    def add_product(self, product: ProductDataDto):
        logging.info(f"add_product {product}")
        self.products.append(product)

    # def create_basket(self):
    #     basket = Basket()
    #     self.baskets.append(basket)
    #     return basket
    #
    # def delete_basket(self, id):
    #     if id < len(self.baskets):
    #         del self.baskets[id]
    #         return True
    #     return False
    #
    # def get_basket(self, id):
    #     if id < len(self.baskets):
    #     return None
    #         return self.baskets[id]
