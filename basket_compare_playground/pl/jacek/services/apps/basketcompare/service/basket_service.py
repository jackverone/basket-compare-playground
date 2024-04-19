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
        # basket_compare = {}  # type: Dict[(int, int), List[ProductDataDto]]
        basket_compare = {}  # type: Dict[(int, int), list]

        for product in products:
            for k, v in product.product_data.data.items():
                # basket_compare_key = (v.shop_id, product.product_data.name)
                basket_compare_key = (v.shop_id, v.id)
                # basket_compare_key = v.shop_id
                if basket_compare_key in basket_compare:
                    basket_compare[basket_compare_key].append(v)
                else:
                    basket_compare[basket_compare_key] = [v]

        # logging.info(f"create_basket_compare() = {basket_compare}")
        return basket_compare
