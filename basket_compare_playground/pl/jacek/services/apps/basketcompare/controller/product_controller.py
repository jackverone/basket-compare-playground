import logging

from basket_compare_playground.pl.jacek.services.apps.basketcompare.repository.ProductRepository import ProductRepository
from basket_compare_playground.pl.jacek.services.apps.basketcompare.service.product_service import ProductService
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_meta_data import ProductMetaData


class ProductController:
    def __init__(self, service, repository):
        self.service = service
        self.repository = repository

    def search_product_meta_data(self, name, info) -> ProductMetaData:
        logging.info(f"search_product_meta_data({name}, {info})")
        return self.service.search_product_meta_data(name, info)

    def search_product(self, name, info):
        logging.info(f"search_product({name}, {info})")
        return self.service.search_product_full_data(name, info)

    def create_product(self, name, price):
        return self.service.create_product(name, price)

    def get_product(self, name):
        return self.service.get_product(name)

    def update_product(self, name, price):
        return self.service.update_product(name, price)

    def delete_product(self, name):
        return self.service.delete_product(name)
