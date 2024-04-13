import logging
from typing import Dict


class Book:
    def __init__(self, data: Dict):
        self.shops_count = data.get('shopsCount')
        self.min_price = data.get('minPrice')
        self.max_price = data.get('maxPrice')

    def to_dict(self) -> Dict:
        return {
            "shops_count": self.shops_count,
            "min_price": self.min_price,
            "max_price": self.max_price
        }

    def __str__(self):
        return f"Book(shops_count={self.shops_count}, min_price={self.min_price}, max_price={self.max_price})"
