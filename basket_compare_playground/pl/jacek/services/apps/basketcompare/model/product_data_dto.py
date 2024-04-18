import logging

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.BuyBoxData import BuyBoxData


class ProductDataDto:
    """
    Class to store product data, used as wrapper
    for BuyBoxData class which is BuyBox API model.
    """

    def __init__(self):
        self.product_data = None

    def convert_buybox_to_dto(self, buybox_data: BuyBoxData):
        # logging.info(f"convert_buybox_to_dto({buybox_data})")
        logging.info(f"convert_buybox_to_dto(buybox_data)")
        self.product_data = buybox_data
        # logging.info(f"convert_buybox_to_dto() = {self.product_data}")
        logging.info(f"convert_buybox_to_dto() = self.product_data")
        # return self.product_data

    def to_dict(self):
        return {
            "product_data": self.product_data.to_dict()
        }

    def __str__(self):
        return f'ProductDataDto(product_data={str(self.product_data)})'

    def __repr__(self):
        return f'ProductDataDto(product_data={str(self.product_data)})'
