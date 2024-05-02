import logging

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model import BuyBoxData
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_meta_data import ProductMetaData


def from_buybox_data(buybox_data: BuyBoxData) -> ProductMetaData:
    logging.info(f"from_buybox_data(buybox_data)")
    # product_meta_data = ProductMetaData(
    logging.info(f"from_buybox_data(...) = ")
    return None
