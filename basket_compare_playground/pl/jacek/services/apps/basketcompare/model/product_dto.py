from typing import List

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product import Product
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_meta_data import ProductMetaData


class ProductDto:
    def __init__(self, products: List[Product], product_meta_data: ProductMetaData = None, shop_name: str = None):
        self.products = products
        self.product_meta_data = product_meta_data
        self.shop_name = shop_name

    def __str__(self):
        return (f"ProductDto(products={self.products}, product_meta_data={self.product_meta_data}, "
                f"shop_name={self.shop_name})")

    def __repr__(self):
        return self.__str__()
