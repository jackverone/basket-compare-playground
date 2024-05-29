import logging
from typing import List

from basket_compare_playground.pl.jacek.services.apps.basketcompare.service.basket_service import BasketService
from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model import BuyBoxData
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_search_dto import ProductSearchDto


class BasketController:
    def __init__(self, service: BasketService):
        self.service = service

    def get_all_products(self):
        logging.info(f"get_all_products()")
        return self.service.get_all_products()

    def search_and_add_product(self, name, info):
        logging.info(f"search_and_add_product({name}, {info})")
        product = self.service.search_and_add_product(name, info)
        return product

    def search_by_dto_and_add_product(self, product_search_dto: ProductSearchDto):
        logging.info(f"search_by_dto_and_add_product({product_search_dto})")
        product = self.service.search_and_add_product(product_search_dto)
        return product

    def create_basket_compare(self, products: List[BuyBoxData]):
        # logging.info(f"create_basket_compare({products})")
        logging.info(f"create_basket_compare(products)")
        return self.service.create_basket_compare_(products)
