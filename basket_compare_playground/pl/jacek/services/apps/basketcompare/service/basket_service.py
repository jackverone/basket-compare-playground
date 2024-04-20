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
        # initial_basket_compare = {}  # type: Dict[(int, int), List[ProductDataDto]]
        initial_basket_compare = {}  # type: Dict[(int, int), list]

        for product in products:
            for k, v in product.product_data.data.items():
                basket_compare_key = (v.shop_id, v.name)
                v.product_name = product.product_data.name
                if basket_compare_key in initial_basket_compare:
                    initial_basket_compare[basket_compare_key].append(v)
                else:
                    initial_basket_compare[basket_compare_key] = [v]

        for basket_compare_key, products in initial_basket_compare.items():
            sorted_datum_products = sort_datum_products(products)
            initial_basket_compare[basket_compare_key] = sorted_datum_products

        products_count = 0
        product_names = []
        products_len = len(products)

        final_basket_compare = {}

        for k, v in initial_basket_compare.items():
            for product in v:
                if products_count <= products_len:
                    if product.product_name not in product_names:
                        products_count += 1
                        product_names.append(product.product_name)
                        # logging.info(f"product_names = {product_names}")
                        # logging.info(f"create_basket_compare() = {k} -> {product}")
                        if k in final_basket_compare:
                            final_basket_compare[k].append(product)
                        else:
                            final_basket_compare[k] = [product]
                else:
                    products_count = 0
                    product_names = []
                    break

        final_basket_compare_keys_to_remove = []

        for k, v in final_basket_compare.items():
            if len(v) != products_len + 1:
                final_basket_compare_keys_to_remove.append(k)

        for k in final_basket_compare_keys_to_remove:
            final_basket_compare.pop(k)

        # first_elements = {key: value[0] for key, value in initial_basket_compare.items() if value}
        # logging.info(f"create_basket_compare() = {first_elements}")

        # for k, v in final_basket_compare.items():
        #     logging.info(f"create_basket_compare: k={k}, v={v} \n")
        #     for product in v:
        #         logging.info(f"create_basket_compare: product={product} \n")

        # logging.info(f"create_basket_compare() = {initial_basket_compare}")
        return final_basket_compare
