import logging

from unittest import TestCase

from basket_compare_playground.pl.jacek.services.apps.basketcompare.mapper.product_meta_data_mapper import \
    from_buybox_data
from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.BuyBoxData import \
    BuyBoxData
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_meta_data import ProductMetaData


class Test(TestCase):

    def setUp(self):
        logging.basicConfig(
            level=logging.INFO,
            format="[%(asctime)s] %(levelname)s in %(filename)s %(module)s %(funcName)s: %(message)s"
        )

    def test_from_buybox_data(self):
        # Given
        json_data = {
            "status": True,
            "spaceId": 7110,
            "trackingUrl": "",
            "sortType": "1",
            "useCSS": True,
            "useTabs": True,
            "defaultTab": 0,
            "leadColor": "#666666",
            "showProduct": True,
            "shopStyle": "icon_name",
            "version": "latest",
            "language": "pl",
            "showPrices": True,
            "sendGaClientId": False,
            "buttonLabel": "Idź do sklepu »",
            "rowCount": 10,
        }
        buybox_data = BuyBoxData(json_data)

        # When
        product_meta_data: ProductMetaData = from_buybox_data(buybox_data)

        # Then
        self.assertEqual(buybox_data.status, product_meta_data.status, "Status should be the same")
        self.assertEqual(buybox_data.space_id, product_meta_data.space_id, "Space ID should be the same")
