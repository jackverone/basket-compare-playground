from typing import List

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product import Product


class ProductDto:
    def __init__(self, products: List[Product]):
        self.products = products

    def __str__(self):
        return f"ProductDto(products={str(self.products)})"
