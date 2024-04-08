import logging
import json

from unittest import TestCase

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_data_dto import ProductDataDto
from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.BuyBoxData import \
    BuyBoxData


class TestProductDataDto(TestCase):

    def setUp(self):
        logging.basicConfig(level=logging.DEBUG)
        self.product_data_dto = ProductDataDto()

    buybox_json = """
{
  "status": true,
  "data": {
    "https://go.buybox.click/bbclick_17970_169801879": {
      "id": 169801879,
      "name": "TaniaKsiazka.pl",
      "icon": "https://assets.buybox.click/9e1bc1cb3c94dd5d1170ac98a276c39a77d5e70f.png",
      "logo": "https://assets.buybox.click/e6a7c997c7d1e4ead0cfad88e225a2e782813554.png",
      "type": "audiobook",
      "typeId": 3,
      "typeName": "audiobook",
      "shopId": 11,
      "currency": "PLN",
      "price": "14.57"
    },
    "https://go.buybox.click/bbclick_17970_193153244": {
      "id": 193153244,
      "name": "Legimi",
      "icon": "https://assets.buybox.click/5d826a78650f0ec8eca2900d28035ea605514be3.png",
      "logo": "https://assets.buybox.click/6b6f67f35b5e1c138dd2ad2bd7032fda9528f2c5.png",
      "type": "audiobook",
      "typeId": 3,
      "typeName": "audiobook",
      "shopId": 9,
      "currency": "PLN",
      "price": "14.99",
      "pricePrefix": "od"
    }
  },
  "spaceId": 7110,
  "trackingUrl": "",
  "sortType": "1",
  "useCSS": true,
  "useTabs": true,
  "defaultTab": 0,
  "leadColor": "#666666",
  "showProduct": true,
  "shopStyle": "icon_name",
  "version": "latest",
  "language": "pl",
  "showPrices": true,
  "sendGaClientId": false,
  "buttonLabel": "Idź do sklepu »",
  "rowCount": 10,
  "statistics": {
    "shopsCount": 23,
    "minPrice": "14.57",
    "maxPrice": "207.00",
    "currency": "PLN",
    "byType": {
      "audiobook": {
        "shopsCount": 12,
        "minPrice": "14.57",
        "maxPrice": "99.90"
      },
      "book": {
        "shopsCount": 19,
        "minPrice": "24.72",
        "maxPrice": "207.00"
      },
      "ebook": {
        "shopsCount": 5,
        "minPrice": "25.65",
        "maxPrice": "33.00"
      }
    }
  },
  "name": "Alchemik",
  "info": "Paulo Coelho",
  "image": "https://cf-tk.statiki.pl/images/thumbs/D30/50266701622CD.jpg"
}
    """

    def test_convert_buybox_tod_dto(self):
        buybox_data = BuyBoxData(json.loads(self.buybox_json))
        self.product_data_dto.convert_buybox_to_dto(buybox_data)

        self.assertIsNotNone(self.product_data_dto, "Product data should not be None")
