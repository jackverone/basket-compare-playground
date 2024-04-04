import logging
from typing import Dict


class Book:
    def __init__(self, data: Dict):
        self.shops_count = data.get('shopsCount')
        self.min_price = data.get('minPrice')
        self.max_price = data.get('maxPrice')

    # shops_count: int
    # min_price: str
    # max_price: str
    #
    # def __init__(self, json_data):
    #     if json_data is None:
    #         logging.error("Book: json_data is None")
    #         json_data = {}
    #
    #     self.shops_count = json_data.get("shopsCount", 0)
    #     self.min_price = json_data.get("minPrice", "0")
    #     self.max_price = json_data.get("maxPrice", "0")

    def __str__(self):
        return f"Book(shops_count={self.shops_count}, min_price={self.min_price}, max_price={self.max_price})"
