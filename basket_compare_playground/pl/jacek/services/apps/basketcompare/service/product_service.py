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

        # product_dto.products = sorted(product_dto.products, key=lambda x: (x.type, x.name))
        # products_grouped_by_type = [ProductDto([product for product in product_dto.products if product.name == name])
        #                             for name in set([product.name for product in product_dto.products])]
        # initial_products_grouped_by_type = {}  # type: Dict[(str, str), List[ProductDto]]

        initial_products_grouped_by_type: List[ProductDto] = []
        unique_products_by_shop_and_product_name = set([(product.product_name, product.shop_id)
                                                        for product in product_dto.products])

        for unique_product in unique_products_by_shop_and_product_name:
            unique_product_dto: ProductDto = ProductDto([])
            for product in product_dto.products:
                if (product.product_name, product.shop_id) == unique_product:
                    unique_product_dto.products.append(product)
                    if unique_product_dto.product_meta_data is None:
                        unique_product_dto.product_meta_data = product.product_meta_data
                        unique_product_dto.product_meta_data.shop_name = product.name
            initial_products_grouped_by_type.append(unique_product_dto)

        initial_products_grouped_by_type = sorted(initial_products_grouped_by_type,
                                                  key=lambda x: len(x.products), reverse=True)

        # for unique_product equals (product.product_name, product.shop_id) append products into ProductDto and add product_meta_data
        # matching_products = [product for product in product_dto.products if (product.product_name, product.shop_id) == unique_product]
        # initial_products_grouped_by_type[unique_product] = [ProductDto(matching_products)]
        # products_grouped_by_type: ProductByTypeDto = ProductByTypeDto([])
        # for key, value in initial_products_grouped_by_type.items():
        #     products_grouped_by_type.product_dtos(value)
        logging.info(f"unique_products_by_shop_and_product_name = {unique_products_by_shop_and_product_name}")
        # initial_products_grouped_by_type = defaultdict(list)
        # for unique_products_by_shop_and_product_name_item in unique_products_by_shop_and_product_name:
        #     initial_products_grouped_by_type[unique_products_by_shop_and_product_name_item] = [ProductDto(List[ProductDto])]
        # for product in product_dto.products:
        #     single_product_dto = ProductDto([product], product.product_meta_data)
        #     initial_products_grouped_by_type[(product.product_name, product.shop_id)].append(single_product_dto)
        # for key, value in initial_products_grouped_by_type.items():
        #     logging.info(f"key = {key}, value = {value}")
        # logging.info(f"value LEN = {len(initial_products_grouped_by_type)}")
        # for key, value in initial_products_grouped_by_type.items():
        #     logging.info(f"value TYPE = {type(value)}")
        #     for product in value:
        #         logging.info(f"product TYPE = {type(product)}")
        # for key, value in initial_products_grouped_by_type.items():
        #     logging.info(f"key = {key}, value = {value} \n")
        # combined_product_dtos = []  # type: # List[ProductDto]
        # product_dtos_values = initial_products_grouped_by_type.values()
        # for product_dto in product_dtos_values:
            # logging.info(f"product_dto.products LEN = {len(product_dto.products)}")
            # combined_product_dtos.append(product_dto)
        # values: List[ProductDto] = [product for sublist in initial_products_grouped_by_type.values() for product in sublist]
        # logging.info(f"initial_products_grouped_by_type values = {len(initial_products_grouped_by_type)}")
        # logging.info(f"combined_product_dtos values = {len(combined_product_dtos)}")
        # products_grouped_by_type = ProductByTypeDto(initial_products_grouped_by_type.values())
        # products_grouped_by_type = ProductByTypeDto([value for value in initial_products_grouped_by_type.values()])

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
