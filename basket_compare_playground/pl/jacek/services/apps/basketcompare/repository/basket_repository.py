import logging
from typing import List

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_dto import ProductDto


class BasketRepository:
    def __init__(self):
        self.baskets = []
        self.products = []  # type: List[ProductDto]

    def get_all_products(self):
        logging.info(f"get_all_products() = products")
        return self.products

    def add_product(self, product: ProductDto) -> ProductDto:
        logging.info(f"add_product(product)")
        self.products.append(product)
        logging.info(f"add_product(...) = product")
        return product

    def clear_all_products(self):
        logging.info(f"clear_all_products()")
        self.products.clear()
