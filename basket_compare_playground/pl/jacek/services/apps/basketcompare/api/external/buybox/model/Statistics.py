import logging
from typing import Dict

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.Currency import Currency
from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.ByType import ByType


class Statistics:
    def __init__(self, data: Dict):
        self.shops_count = data.get('shopsCount')
        self.min_price = data.get('minPrice')
        self.max_price = data.get('maxPrice')
        self.currency = data.get('currency')
        self.by_type = ByType(data.get('byType', {}))

    # shops_count: int
    # min_price: str
    # max_price: str
    # currency: Currency
    # by_type: ByType
    #
    # def __init__(self, json_data):
    #     if json_data is None:
    #         logging.error("Statistics: json_data is None")
    #         json_data = {}
    #
    #     self.shops_count = json_data.get("shopsCount", 0)
    #     self.min_price = json_data.get("minPrice", "0")
    #     self.max_price = json_data.get("maxPrice", "0")
    #     self.currency = Currency(json_data.get("currency", {}))
    #     self.by_type = ByType(json_data.get("byType", {}))

    def __str__(self):
        return (f"Statistics(shops_count={self.shops_count}, min_price={self.min_price}, max_price={self.max_price}, "
                f"currency={self.currency}, by_type={self.by_type})")
