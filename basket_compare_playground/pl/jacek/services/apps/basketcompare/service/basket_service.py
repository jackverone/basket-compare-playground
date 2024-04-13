import logging

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_data_dto import ProductDataDto
from basket_compare_playground.pl.jacek.services.apps.basketcompare.repository.basket_repository import BasketRepository


class BasketService:
    def __init__(self, repository: BasketRepository):
        self.repository = repository

    def get_all_products(self):
        logging.info(f"get_all_products({self.repository.products})")
        return self.repository.get_all_products()

    def add_product(self, product: ProductDataDto):
        logging.info(f"add_product {product}")
        return self.repository.add_product(product)

    # def create_basket(self):
    #     return self.repository.create_basket()
    #
    # def delete_basket(self, id):
    #     return self.repository.delete_basket(id)
    #
    # def get_basket(self, id):
    #     return self.repository.get_basket(id)
