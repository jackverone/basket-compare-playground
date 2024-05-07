import logging

from typing import List

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model import BuyBoxData
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product import Product

from basket_compare_playground.pl.jacek.services.apps.basketcompare.mapper.product_mapper import from_datum

from basket_compare_playground.pl.jacek.services.apps.basketcompare.mapper.product_meta_data_mapper import \
    extract_product_meta_data


def from_buybox_data(buybox_data: BuyBoxData) -> List[Product]:
    logging.info(f"from_buybox_data({buybox_data})")
    products = []  # type: List[Product]

    product_meta_data = extract_product_meta_data(buybox_data)

    for key, datum in buybox_data.data.items():
        product = from_datum(datum)
        # FIXME: use setter instead of direct assignment!
        product.product_meta_data = product_meta_data
        product.product_url = key
        products.append(product)

    logging.info(f"from_buybox_data(...) = products")
    return products
