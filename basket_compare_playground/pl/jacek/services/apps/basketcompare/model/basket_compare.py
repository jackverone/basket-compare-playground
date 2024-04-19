from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.basket import Basket


class BasketCompare:
    def __init__(self):
        self.baskets = []

    def add_basket(self, basket: Basket):
        self.baskets.append(basket)

    def remove_basket(self, basket):
        self.baskets.remove(basket)

    def find_lowest_price_basket(self):
        return min(self.baskets, key=lambda basket: basket.calculate_total_price())
