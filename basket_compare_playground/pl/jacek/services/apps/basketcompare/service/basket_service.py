import logging
from typing import List, Dict

from basket_compare_playground.pl.jacek.services.apps.basketcompare.repository.basket_repository import BasketRepository

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.shop_info import ShopInfo
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.basket_compare import BasketCompare
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.basket import Basket
from basket_compare_playground.pl.jacek.services.apps.basketcompare.mapper.product_mapper import from_datum

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.Datum import Datum
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_data_dto import ProductDataDto
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

        products_len = len(products)
        products_count = 0
        # products_total = 0.0
        product_names = []

        final_basket_compare = {}
        # final_basket_compare_model = {}  # type: Dict[(int, int), List[BasketCompare]]
        # basket_compare_model = BasketCompare()
        final_basket_compare_model = BasketCompare()

        for k, v in initial_basket_compare.items():
            # if k in final_basket_compare_model:
            #     final_basket_compare_model[k].append(basket_compare_model)
            # else:
            # final_basket_compare_model[k] = [basket_compare_model]
            shop_info_model = ShopInfo(k[0], k[1])
            basket_model = Basket()
            basket_model.shop_info = shop_info_model

            for product in v:

                if products_count <= products_len:
                    if product.product_name not in product_names:
                        products_count += 1
                        product_names.append(product.product_name)
                        # products_total += float(product.price)
                        # logging.info(f"product_names = {product_names}")
                        # logging.info(f"create_basket_compare() = {k} -> {product}")

                        shop_info_model.shop_icon_url = product.icon
                        product_from_datum = from_datum(product)
                        basket_model.add_product(product_from_datum)

                        if k in final_basket_compare:
                            final_basket_compare[k].append(product)
                        else:
                            final_basket_compare[k] = [product]
                else:
                    products_count = 0
                    # products_total = 0.0
                    product_names = []
                    break

            final_basket_compare_model.add_basket(basket_model)

        # final_basket_compare_keys_to_remove = []
        #
        # for k, v in final_basket_compare.items():
        #     if len(v) != products_len + 1:
        #         final_basket_compare_keys_to_remove.append(k)
        #
        # for k in final_basket_compare_keys_to_remove:
        #     final_basket_compare.pop(k)

        final_basket_compare_model.baskets = [basket for basket in final_basket_compare_model.baskets if
                                              len(basket.products) == products_len + 1]

        # logging.info(f"final_basket_compare_model: {final_basket_compare_model}")

        # first_elements = {key: value[0] for key, value in initial_basket_compare.items() if value}
        # logging.info(f"create_basket_compare() = {first_elements}")

        # for k, v in final_basket_compare.items():
        #     logging.info(f"create_basket_compare: k={k}, v={v} \n")
        #     for product in v:
        #         logging.info(f"create_basket_compare: product={product} \n")

        # logging.info(f"create_basket_compare() = {initial_basket_compare}")
        return final_basket_compare_model
