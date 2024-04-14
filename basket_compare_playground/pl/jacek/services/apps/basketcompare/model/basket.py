from typing import List, Set, Dict

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product import Product


class Basket:
    def __init__(self):
        self.products = Dict[int, Product]
