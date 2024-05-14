import logging
from typing import Dict, List

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.utils.model_utils import \
    sort_baskets_by_total_price, sort_products_by_price
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_dto import ProductDto
from basket_compare_playground.pl.jacek.services.apps.basketcompare.repository.basket_repository import BasketRepository
from basket_compare_playground.pl.jacek.services.apps.basketcompare.service.product_service import ProductService
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.basket_compare import BasketCompare
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.basket import Basket
from basket_compare_playground.pl.jacek.services.apps.basketcompare.mapper.shop_info_mapper import \
    map_shop_info_from_product


class BasketService:
    def __init__(self, product_service: ProductService, repository: BasketRepository):
        self.product_service = product_service
        self.repository = repository

    def get_all_products(self):
        logging.info(f"get_all_products()")
        all_products = self.repository.get_all_products()
        logging.info(f"get_all_products() = all_products")
        return all_products

    def search_and_add_product(self, name, info):
        logging.info(f"search_and_add_product({name}, {info})")
        product_full_data = self.product_service.search_product_full_data(name, info)
        added_product = self.repository.add_product(product_full_data)
        logging.info(f"search_and_add_product(...) = added_product")
        return added_product

    def add_product(self, product: ProductDto):
        logging.info(f"add_product(product)")
        return self.repository.add_product(product)

    def create_basket_compare_(self, product_dtos: List[ProductDto]) -> BasketCompare:
        basket_compare: BasketCompare = BasketCompare()
        basket_product_classify_dict = {}  # type: Dict[(int, int), Basket]

        # classify products by shop_id for basket creation
        for basket in product_dtos:
            for product in basket.products:
                basket = Basket()
                basket.shop_info = map_shop_info_from_product(product)

                basket_product_classify_dict.setdefault(product.shop_id, basket)
                basket_product_classify_dict[product.shop_id].products.append(product)

        # sort products by price
        for basket_product_classify_dict_key, basket in basket_product_classify_dict.items():
            basket.products = sort_products_by_price(basket.products)
            basket_compare.add_basket(basket)

        # products_len = len(product_dtos)
        # logging.info(f"products_len = {products_len}")
        # products_count = 0
        # products_total = 0.0
        # product_names = []
        unique_products_dict = {}
        total_price = 0.0

        # find unique products and sum total price for each basket
        for basket in basket_compare.baskets.copy():
            for product in basket.products:
                logging.info(f"product = {product}")
                if (product.product_name in unique_products_dict and
                        unique_products_dict[product.product_name].price <= product.price):
                    continue
                elif product.product_name in unique_products_dict:
                    total_price -= unique_products_dict[product.product_name].price

                unique_products_dict[product.product_name] = product
                total_price += product.price

            if len(unique_products_dict.values()) != 2:
                basket_compare.remove_basket(basket)

            basket.total_price = total_price
            basket.products = list(unique_products_dict.values())
            total_price = 0.0
            unique_products_dict = {}

            # sort baskets by total price
            basket_compare.baskets = sort_baskets_by_total_price(basket_compare.baskets)

        return basket_compare

    def create_basket_compare(self, product_dtos: List[ProductDto]):
        logging.info(f"create_basket_compare({len(product_dtos)})")
        initial_basket_compare = {}  # type: Dict[(int, int), list]

        for product_dto in product_dtos:
            for product in product_dto.products:
                basket_compare_key = (product.shop_id, product.product_name)
                # v.product_name = product_dto.name
                if basket_compare_key in initial_basket_compare:
                    initial_basket_compare[basket_compare_key].append(product)
                else:
                    initial_basket_compare[basket_compare_key] = [product]

        for basket_compare_key, product_dtos in initial_basket_compare.items():
            sorted_datum_products = sort_products_by_price(product_dtos)
            initial_basket_compare[basket_compare_key] = sorted_datum_products

        logging.info(f"create_basket_compare() = {initial_basket_compare}")

        '''
        

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
        '''

        return initial_basket_compare
