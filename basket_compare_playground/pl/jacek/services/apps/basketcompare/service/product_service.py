import logging

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.service.BuyBoxService import \
    BuyBoxService
from basket_compare_playground.pl.jacek.services.apps.basketcompare.mapper.buybox_data_mapper import map_products_from_buybox_data
from basket_compare_playground.pl.jacek.services.apps.basketcompare.mapper.product_meta_data_mapper import \
    extract_product_meta_data
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_dto import ProductDto
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_meta_data import ProductMetaData


class ProductService:
    def __init__(self, repository, buybox_service: BuyBoxService):
        self.buybox_service = buybox_service
        self.repository = repository

    def search_product_meta_data(self, name, info) -> ProductMetaData:
        logging.info(f"search_product_meta_data({name}, {info})")
        buybox_result = self.buybox_service.get_buybox_data(name, info)
        product_meta_data = extract_product_meta_data(buybox_result)
        logging.info(f"search_product_meta_data() = {product_meta_data}")
        return product_meta_data

    def search_product_full_data(self, name, info) -> ProductDto:
        logging.info(f"search_product_full_data({name}, {info})")
        buybox_result = self.buybox_service.get_buybox_data(name, info)
        products = map_products_from_buybox_data(buybox_result)
        product_dto = ProductDto(products)
        logging.info(f"search_product_full_data() = product_dto")
        return product_dto

    def create_product(self, name, price):
        logging.info(f"Creating product {name} with price {price}")
        return self.repository.create_product(name, price)

    def get_product(self, name):
        logging.info(f"Getting product {name}")
        return self.repository.get_product(name)

    def delete_product(self, name):
        return self.repository.delete_product(name)

    def update_product(self, name, price):
        return self.repository.update_product(name, price)
