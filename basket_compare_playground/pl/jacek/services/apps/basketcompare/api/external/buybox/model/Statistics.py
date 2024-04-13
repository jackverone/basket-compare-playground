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

    def to_dict(self) -> Dict:
        return {
            "shops_count": self.shops_count,
            "min_price": self.min_price,
            "max_price": self.max_price,
            "currency": self.currency,
            "by_type": self.by_type.to_dict()
        }

    def __str__(self):
        return (f"Statistics(shops_count={self.shops_count}, min_price={self.min_price}, max_price={self.max_price}, "
                f"currency={self.currency}, by_type={self.by_type})")
