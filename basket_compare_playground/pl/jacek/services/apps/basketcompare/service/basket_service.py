import logging
from typing import List, Dict

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_data_dto import ProductDataDto
from basket_compare_playground.pl.jacek.services.apps.basketcompare.repository.basket_repository import BasketRepository

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.Datum import Datum
from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.utils.buybox_data_utils import \
    sort_datum_products


class BasketService:
    def __init__(self, repository: BasketRepository):
        self.repository = repository

    def get_all_products(self):
        logging.info(f"get_all_products()")
        all_products = self.repository.get_all_products()
        logging.info(f"get_all_products() = all_products")
        return all_products

    def add_product(self, product: ProductDataDto):
        # logging.info(f"add_product {product}")
        logging.info(f"add_product(product)")
        return self.repository.add_product(product)

    def create_basket_compare(self, products: List[ProductDataDto]):
        # logging.info(f"create_basket_compare({str(products)})")
        logging.info(f"create_basket_compare({len(products)})")
        # basket_compare = {}  # type: Dict[(int, int), List[ProductDataDto]]
        basket_compare = {}  # type: Dict[(int, int), list]

        products_len = len(products)
        for product in products:
            for k, v in product.product_data.data.items():
                basket_compare_key = (v.shop_id, v.name)
                v.product_name = product.product_data.name
                if basket_compare_key in basket_compare:
                    basket_compare[basket_compare_key].append(v)
                else:
                    basket_compare[basket_compare_key] = [v]

        for basket_compare_key, products in basket_compare.items():
            sorted_datum_products = sort_datum_products(products)
            basket_compare[basket_compare_key] = sorted_datum_products

        products_count = 0
        for k, v in basket_compare.items():
            # logging.info(f"create_basket_compare() = {k} -> {v}")
            product_id = 0
            for product in v:
                if product.id != product_id:
                    if products_count < products_len:
                        products_count += 1
                        product_id = product.id
                        logging.info(f"create_basket_compare() = {k} -> {product}")
                    else:
                        products_count = 0

        # first_elements = {key: value[0] for key, value in basket_compare.items() if value}
        # logging.info(f"create_basket_compare() = {first_elements}")

        # logging.info(f"create_basket_compare() = {basket_compare}")
        return basket_compare
