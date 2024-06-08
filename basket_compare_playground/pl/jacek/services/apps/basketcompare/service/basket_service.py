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
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_search_dto import ProductSearchDto
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product import Product


class BasketService:
    def __init__(self, product_service: ProductService, repository: BasketRepository):
        self.product_service = product_service
        self.repository = repository

    def get_all_products(self) -> List[ProductDto]:
        logging.info(f"get_all_products()")
        all_products = self.repository.get_all_products()
        logging.info(f"get_all_products() = all_products")
        return all_products

    def search_and_add_product(self, name, info):
        logging.info(f"search_and_add_product({name}, {info})")
        product_full_data = self.product_service.search_product_full_data(name, info)
        added_product = self.repository.add_product_dto(product_full_data)
        logging.info(f"search_and_add_product(...) = added_product")
        return added_product

    def search_by_type_and_add_product(self, product_search_dto: ProductSearchDto) -> ProductDto:
        logging.info(f"search_by_type_and_add_product({product_search_dto})")

        found_product_full_data = self.product_service.search_product_full_data(
            product_search_dto.name, product_search_dto.info)

        products = [product for product in found_product_full_data.products if product.type == product_search_dto.type]
        added_product_dto = self.repository.add_product_dto(ProductDto(products))

        logging.info(f"search_by_type_and_add_product(...) = added_product_dto")
        return added_product_dto

    # def add_product(self, product: ProductDto):
    #     logging.info(f"add_product(product)")
    #     return self.repository.add_product_dto(product)

    def create_basket_compare(self, product_dtos: List[ProductDto]) -> BasketCompare:
        logging.info(f"create_basket_compare(product_dtos)")
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

        unique_products_dict = {}
        total_price = 0.0

        # find unique products and sum total price for each basket
        for basket in basket_compare.baskets.copy():
            for product in basket.products:
                if (product.product_name in unique_products_dict and
                        unique_products_dict[product.product_name].price <= product.price):
                    continue
                elif product.product_name in unique_products_dict:
                    total_price -= unique_products_dict[product.product_name].price

                unique_products_dict[product.product_name] = product
                total_price += product.price

            if len(unique_products_dict.values()) != len(product_dtos):
                basket_compare.remove_basket(basket)

            basket.total_price = total_price
            basket.products = list(unique_products_dict.values())
            total_price = 0.0
            unique_products_dict = {}

            # sort baskets by total price
            basket_compare.baskets = sort_baskets_by_total_price(basket_compare.baskets)

        logging.info(f"create_basket_compare(...) = basket_compare")
        return basket_compare
