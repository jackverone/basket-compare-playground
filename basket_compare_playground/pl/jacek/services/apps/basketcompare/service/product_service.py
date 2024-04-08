import logging

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.service.BuyBoxService import BuyBoxService


class ProductService:
    def __init__(self, repository):
        self.buybox_service = BuyBoxService()
        self.repository = repository

    def search_product(self, name, info):
        logging.info(f'Searching product {name} with info {info}')
        buybox_result = self.buybox_service.get_buybox_data(name, info)
        logging.info(f'BuyBoxData: {buybox_result}')
        return buybox_result

    def create_product(self, name, price):
        logging.info(f'Creating product {name} with price {price}')
        return self.repository.create_product(name, price)

    def get_product(self, name):
        logging.info(f'Getting product {name}')
        return self.repository.get_product(name)

    def delete_product(self, name):
        return self.repository.delete_product(name)

    def update_product(self, name, price):
        return self.repository.update_product(name, price)
