import logging
from collections import defaultdict
from typing import Dict, List, Set

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.service.BuyBoxService import \
    BuyBoxService
from basket_compare_playground.pl.jacek.services.apps.basketcompare.mapper.buybox_data_mapper import \
    map_products_from_buybox_data
from basket_compare_playground.pl.jacek.services.apps.basketcompare.mapper.product_meta_data_mapper import \
    extract_product_meta_data
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_dto import ProductDto
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_meta_data import ProductMetaData
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_search_dto import ProductSearchDto
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_by_type_dto import ProductByTypeDto


class ProductService:
    def __init__(self, repository, buybox_service: BuyBoxService):
        self.buybox_service = buybox_service
        self.repository = repository

    def search_product_meta_data(self, name, info) -> ProductMetaData:
        logging.info(f"search_product_meta_data({name}, {info})")
        buybox_result = self.buybox_service.get_buybox_data(name, info)
        product_meta_data = extract_product_meta_data(buybox_result)
        logging.info(f"search_product_meta_data() = {product_meta_data}")
        return product_meta_data

    def search_product_full_data(self, name, info) -> ProductDto:
        logging.info(f"search_product_full_data({name}, {info})")
        buybox_result = self.buybox_service.get_buybox_data(name, info)
        products = map_products_from_buybox_data(buybox_result)
        product_dto = ProductDto(products)
        logging.info(f"search_product_full_data() = product_dto")
        return product_dto

    def search_product_grouped_by_type_full_data(self, product_search_dto: ProductSearchDto) -> ProductByTypeDto:
        logging.info(f"search_product_grouped_by_type_full_data({product_search_dto})")
        product_dto: ProductDto = self.search_product_full_data(product_search_dto.name, product_search_dto.info)

        initial_products_grouped_by_type: List[ProductDto] = []
        unique_products_by_shop_and_product_name = (
            set([(product.product_name, product.name, product.shop_id) for product in product_dto.products]))

        for unique_product in unique_products_by_shop_and_product_name:
            unique_product_dto: ProductDto = ProductDto([])
            for product in product_dto.products:
                if (product.product_name, product.name, product.shop_id) == unique_product:
                    unique_product_dto.products.append(product)
                    unique_product_dto.product_meta_data = product.product_meta_data
                    unique_product_dto.product_meta_data.shop_name = product.name
                    unique_product_dto.shop_name = product.name
            initial_products_grouped_by_type.append(unique_product_dto)

        initial_products_grouped_by_type = sorted(initial_products_grouped_by_type,
                                                  key=lambda x: len(x.products), reverse=True)

        logging.info(f"search_product_grouped_by_type_full_data() = initial_products_grouped_by_type")
        return ProductByTypeDto(initial_products_grouped_by_type)

    def create_product(self, name, price):
        logging.info(f"Creating product {name} with price {price}")
        return self.repository.create_product(name, price)

    def get_product(self, name):
        logging.info(f"Getting product {name}")
        return self.repository.get_product(name)

    def delete_product(self, name):
        return self.repository.delete_product(name)

    def update_product(self, name, price):
        return self.repository.update_product(name, price)
