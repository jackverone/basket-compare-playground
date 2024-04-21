from typing import List

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.basket import Basket


class BasketCompare:
    def __init__(self):
        self.baskets = []  # type: List[Basket]

    def add_basket(self, basket: Basket):
        self.baskets.append(basket)

    def remove_basket(self, basket):
        self.baskets.remove(basket)

    def __str__(self):
        return f"baskets={self.baskets}"

    def __repr__(self):
        return self.__str__()
