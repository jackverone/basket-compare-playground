import logging

from typing import List

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model import BuyBoxData
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product import Product

from basket_compare_playground.pl.jacek.services.apps.basketcompare.mapper.product_mapper import map_product_from_datum

from basket_compare_playground.pl.jacek.services.apps.basketcompare.mapper.product_meta_data_mapper import \
    extract_product_meta_data


def map_products_from_buybox_data(buybox_data: BuyBoxData) -> List[Product]:
    # logging.info(f"from_buybox_data(buybox_data)")
    products = []  # type: List[Product]

    product_meta_data = extract_product_meta_data(buybox_data)

    if hasattr(buybox_data, 'data'):
        for key, datum in buybox_data.data.items():
            product = map_product_from_datum(datum)
            product.product_meta_data = product_meta_data
            product.product_url = key
            product.product_name = product_meta_data.name
            product.product_info = product_meta_data.info
            products.append(product)

    # logging.info(f"from_buybox_data(...) = products")
    return products
