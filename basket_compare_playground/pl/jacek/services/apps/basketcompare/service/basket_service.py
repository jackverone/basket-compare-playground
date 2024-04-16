import logging
from typing import List, Dict

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_data_dto import ProductDataDto
from basket_compare_playground.pl.jacek.services.apps.basketcompare.repository.basket_repository import BasketRepository

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.Datum import Datum


class BasketService:
    def __init__(self, repository: BasketRepository):
        self.repository = repository

    def get_all_products(self):
        logging.info(f"get_all_products()")
        all_products = self.repository.get_all_products()

        # product_data_dtos = [product_data_dto.convert_buybox_to_dto(product) for product in all_products]
        # product_data_dtos = []
        # for product in all_products:
        #     product_data_dto = ProductDataDto()
        #     product_data_dto.convert_buybox_to_dto(product)
        #     product_data_dtos.append(product_data_dto)
        # logging.info(f"product_data_dtos={product_data_dtos}")

        logging.info(f"get_all_products() = {all_products}")
        return all_products

    def add_product(self, product: ProductDataDto):
        logging.info(f"add_product {product}")
        return self.repository.add_product(product)

    def create_basket_compare(self, products: List[ProductDataDto]):
        logging.info(f"create_basket_compare({str(products)})")
        basket_compare = {}  # type: Dict[int, List[ProductDataDto]]

        for initial_product in products:
            # logging.info(f"initial_product={vars(initial_product)}")
            # initial_product_data = initial_product.product_data
            # logging.info(f"initial_product_data={vars(initial_product_data)}")
            basket = []

            for another_product in products:
                logging.info(f"another_product={another_product}")
                # another_product_data = another_product.product_data
                # logging.info(f"another_product_data={another_product_data}")

                # initial_product_data_datum: Dict[str, Datum] = initial_product_data.data
                # logging.info(f"initial_product_data_datum={initial_product_data_datum}")
                # another_product_data_datum: Dict[str, Datum] = another_product_data.data
                # logging.info(f"another_product_data_datum={another_product_data_datum}")

                for initial_k, initial_v in initial_product.product_data.data.items():
                    for another_k, another_v in another_product.product_data.data.items():
                        if initial_v.shop_id == another_v.shop_id:
                            basket.append(another_product)

                basket_compare[initial_v.shop_id] = basket

        logging.info(f"create_basket_compare={str(basket_compare)}")
        logging.info(f"create_basket_compare LEN={len(basket_compare)}")
        for k, v in basket_compare.items():
            logging.info(f"create_basket_compare: k={str(k)}, v={str(v)}")
        return basket_compare
