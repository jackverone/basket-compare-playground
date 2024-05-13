from typing import List
from unittest import TestCase

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.utils.buybox_data_utils import \
    sort_products_by_price
from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.Datum import Datum


class Test(TestCase):
    def test_sort_datum(self):
        basket = []  # type: List[Datum]

        datum_alchemik_empik = Datum(datum_alchemik_empik_data)
        datum_alchemik_legimi = Datum(datum_alchemik_legimi_data)
        datum_alchemik_audiotek = Datum(datum_alchemik_audioteka_data)

        basket.append(datum_alchemik_empik)
        basket.append(datum_alchemik_legimi)
        basket.append(datum_alchemik_audiotek)

        print(f"basket before sorting: {basket}")

        sorted_datum = sort_products_by_price(basket)

        print(f"basket after sorting: {sorted_datum}")


datum_alchemik_empik_data = {
    "id": 1,
    "name": "Alchemik",
    "icon": "https://www.alchemik.pl/favicon.ico",
    "logo": "https://www.alchemik.pl/logo.png",
    "type": "shop",
    "typeId": 1,
    "typeName": "shop",
    "shopId": 1,
    "currency": "PLN",
    "price": 22.90,
    "pricePrefix": "od"
}
datum_alchemik_legimi_data = {
    "id": 2,
    "name": "Alchemik",
    "icon": "https://www.legimi.pl/favicon.ico",
    "logo": "https://www.legimi.pl/logo.png",
    "type": "shop",
    "typeId": 1,
    "typeName": "shop",
    "shopId": 2,
    "currency": "PLN",
    "price": 14.99,
    "pricePrefix": "od"
}
datum_alchemik_audioteka_data = {
    "id": 3,
    "name": "Alchemik",
    "icon": "https://www.audioteka.com/favicon.ico",
    "logo": "https://www.audioteka.com/logo.png",
    "type": "shop",
    "typeId": 1,
    "typeName": "shop",
    "shopId": 3,
    "currency": "PLN",
    "price": 14.57,
    "pricePrefix": "od"
}
