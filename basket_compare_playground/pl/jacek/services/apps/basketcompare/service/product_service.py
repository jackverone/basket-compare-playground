import logging

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.service.BuyBoxService import \
    BuyBoxService
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_data_dto import ProductDataDto
from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model import BuyBoxData


class ProductService:
    def __init__(self, repository, buybox_service: BuyBoxService):
        self.buybox_service = buybox_service
        self.repository = repository

    def search_product(self, name, info) -> BuyBoxData:
        logging.info(f"search_product({name}, {info})")
        buybox_result = self.buybox_service.get_buybox_data(name, info)
        product_data_dto = ProductDataDto()
        product_data_dto.convert_buybox_to_dto(buybox_result)
        # logging.info(f"search_product() = {product_data_dto}")
        logging.info(f"search_product() = product_data_dto")
        return buybox_result

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
