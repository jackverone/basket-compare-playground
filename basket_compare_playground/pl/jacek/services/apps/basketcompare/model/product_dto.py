from typing import List

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product import Product
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_meta_data import ProductMetaData


class ProductDto:
    def __init__(self, products: List[Product], product_meta_data: ProductMetaData = None):
        self.products = products
        self.product_meta_data = product_meta_data

    def __str__(self):
        return f"ProductDto(products={str(self.products)}, product_meta_data={str(self.product_meta_data)})"

    def __repr__(self):
        return self.__str__()
