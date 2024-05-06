from typing import List, Dict, Optional

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.shop_info import ShopInfo
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product import Product


class Basket:
    def __init__(self):
        # self.products = Dict[int, Product]
        self.shop_info = None  # type: Optional[ShopInfo]
        self.products = []  # type: List[Product]
        self.total_price = 0.0

    def add_product(self, product: Product):
        self.products.append(product)
        self.total_price += round(float(product.price), 2)

    def to_dict(self):
        return {
            "shop_info": self.shop_info.to_dict(),
            "products": [product.to_dict() for product in self.products],
            "total_price": self.total_price
        }

    def __str__(self):
        return f"shop_info={self.shop_info}, products={self.products}, total_price={self.total_price}"

    def __repr__(self):
        return self.__str__()
