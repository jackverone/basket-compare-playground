import logging
from typing import List

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_data_dto import ProductDataDto
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product import Product
from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model import BuyBoxData


class BasketRepository:
    def __init__(self):
        self.baskets = []
        self.products = []  # type: List[ProductDataDto]
        self.products_ = []  # type: List[Product]
        self.products_from_api = []  # type: List[BuyBoxData]

    def get_all_products(self):
        # logging.info(f"get_all_products() = {self.products}")
        logging.info(f"get_all_products() = products_from_api")
        return self.products_from_api

    def add_product(self, product: ProductDataDto):
        # logging.info(f"add_product {product}")
        logging.info(f"add_product(product)")
        self.products.append(product)

    def add_product_from_api(self, product: BuyBoxData):
        logging.info(f"add_product_from_api(product)")
        self.products_from_api.append(product)

    def add_product_(self, product: Product):
        logging.info(f"add_product_(product)")
        self.products_.append(product)

    def clear_all_products(self):
        logging.info(f"clear_all_products()")
        self.products.clear()
