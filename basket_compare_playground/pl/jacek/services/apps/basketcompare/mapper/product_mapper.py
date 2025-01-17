import logging

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.Datum import Datum
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product import Product


def map_product_from_datum(datum: Datum) -> Product:
    # logging.info(f"map_product_from_datum(datum)")
    product = Product(
        datum.id,
        datum.name,
        datum.icon, datum.logo,
        datum.type, datum.type_id, datum.type_name,
        datum.shop_id, datum.currency,
        float(datum.price), datum.price_prefix
    )
    # logging.info(f"map_product_from_datum() = product")
    return product
