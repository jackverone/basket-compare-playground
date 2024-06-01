from typing import List

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_dto import ProductDto


class ProductByTypeDto:
    def __init__(self, product_dtos: List[ProductDto]):
        self.product_dtos = product_dtos

    def __str__(self):
        return f"ProductByTypeDto(product_by_type={str(self.product_dtos)})"

    def __repr__(self):
        return self.__str__()
