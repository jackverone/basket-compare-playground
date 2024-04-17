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

        # logging.info(f"get_all_products() = {all_products}")
        logging.info(f"get_all_products() = all_products")
        return all_products

    def add_product(self, product: ProductDataDto):
        # logging.info(f"add_product {product}")
        logging.info(f"add_product(product)")
        return self.repository.add_product(product)

    def create_basket_compare(self, products: List[ProductDataDto]):
        # logging.info(f"create_basket_compare({str(products)})")
        logging.info(f"create_basket_compare(products)")
        basket_compare = {}  # type: Dict[int, List[ProductDataDto]]

        for i in range(len(products)):
            initial_product = products[i]
            # for initial_product in products:
            basket = []

            for j in range(i + 1, len(products)):
                another_product = products[j]
                # for another_product in products:

                for initial_k, initial_v in initial_product.product_data.data.items():
                    for another_k, another_v in another_product.product_data.data.items():
                        logging.info(f"initial_v={str(initial_v.shop_id)}, another_v={str(another_v.shop_id)}")
                        if initial_v.shop_id == another_v.shop_id:
                            # and initial_v.price == another_v.price):
                            if initial_v.shop_id in basket_compare:
                                basket_compare[initial_v.shop_id].append(initial_product)
                            else:
                                basket_compare[initial_v.shop_id] = [initial_product]

                        # if initial_v.shop_id == another_v.shop_id:
                        #     basket.append(another_product)
                        #     basket_compare[initial_v.shop_id] = basket

        # logging.info(f"create_basket_compare={str(basket_compare)}")
        # logging.info(f"create_basket_compare LEN={len(basket_compare)}")
        # for k, v in basket_compare.items():
        #     logging.info(f"create_basket_compare: k={str(k)}, v={str(v)} \n")

        # logging.info(f"create_basket_compare() = {basket_compare}")
        return basket_compare
