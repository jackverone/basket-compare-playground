import logging
from typing import List, Dict

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_data_dto import ProductDataDto
from basket_compare_playground.pl.jacek.services.apps.basketcompare.repository.basket_repository import BasketRepository

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.Datum import Datum


class BasketService:
    def __init__(self, repository: BasketRepository):
        self.repository = repository

    def get_all_products(self):
        logging.info(f"get_all_products({self.repository.products})")
        return self.repository.get_all_products()

    def add_product(self, product: ProductDataDto):
        logging.info(f"add_product {product}")
        return self.repository.add_product(product)

    def create_basket_compare(self, products: List[ProductDataDto]):
        logging.info(f"create_basket_compare({products})")
        basket_compare = {}  # type: Dict[int, List[ProductDataDto]]

        for initial_product in products:
            initial_product_data = initial_product.product_data
            basket = []

            for another_product in products:
                another_product_data = another_product.product_data

                initial_product_data_datum: Dict[str, Datum] = initial_product_data.data
                logging.info(f"initial_product_data_datum={initial_product_data_datum}")
                another_product_data_datum: Dict[str, Datum] = another_product_data.data
                logging.info(f"another_product_data_datum={another_product_data_datum}")

                for initial_k, initial_v in initial_product_data_datum.items():
                    for another_k, another_v in another_product_data_datum.items():
                        if initial_v.shop_id == another_v.shop_id:
                            basket.append(another_product)

                basket_compare[initial_v.shop_id] = basket

        logging.info(f"create_basket_compare={basket_compare}")
        logging.info(f"create_basket_compare LEN={len(basket_compare)}")
        for k, v in basket_compare.items():
            logging.info(f"create_basket_compare: k={k}, v={v}")
        return basket_compare
