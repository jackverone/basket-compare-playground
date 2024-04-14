from typing import List, Set, Dict

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_data_dto import ProductDataDto


class Basket:
    def __init__(self):
        self.product_data_dtos = {}  # type: Dict[str, ProductDataDto]
