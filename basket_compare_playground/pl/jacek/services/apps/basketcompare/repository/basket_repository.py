import logging
from typing import List

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_dto import ProductDto
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product import Product


class BasketRepository:
    def __init__(self):
        self.baskets = []
        self.products = []  # type: List[Product]
        self.product_dtos = []  # type: List[ProductDto]

    def get_all_products(self) -> List[ProductDto]:
        logging.info(f"get_all_products() = product_dtos")
        return self.product_dtos

    # def add_product(self, product: Product) -> Product:
    #     logging.info(f"add_product(product)")
    #     self.products.append(product)
    #     logging.info(f"add_product(...) = product")
    #     return product

    def add_product_dto(self, product_dto: ProductDto) -> ProductDto:
        logging.info(f"add_product_dto(product)")
        self.product_dtos.append(product_dto)
        logging.info(f"add_product_dto(...) = product")
        return product_dto

    def clear_all_products(self):
        logging.info(f"clear_all_products()")
        self.product_dtos.clear()
