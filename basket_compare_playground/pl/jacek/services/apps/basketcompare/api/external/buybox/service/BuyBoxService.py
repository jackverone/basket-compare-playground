import traceback
import logging
import requests
import json

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.BuyBoxData import \
    BuyBoxData
from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.constants import BUYBOX_API_URL
from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.constants import BUYBOX_API_ID


class BuyBoxService:
    def __init__(self, base_url=BUYBOX_API_URL):
        self.base_url = base_url

    def get_buybox(self, bb_id, name, name_value, info, info_value):
        logging.info(f"Getting buybox with {bb_id} for {name}={name_value}")

        url = f"{self.base_url}/{bb_id}/buybox.json?{name}={name_value}&{info}={info_value}"
        response = requests.get(url)

        logging.info(f"response: {response}")
        return response

    def get_buybox_data(self, name_value, info_value):
        logging.info(f"Getting buybox data for {name_value} and {info_value}")

        json_data = dict()
        try:
            json_data = self.get_buybox(BUYBOX_API_ID, "name", name_value, "info", info_value)
            parsed_json = json.loads(json_data.text)
            buy_box_data = BuyBoxData(parsed_json)
            buy_box_data.sort_data_by_price()

            logging.info(f"BuyBoxData: {str(buy_box_data)}")
        except TypeError as e:
            logging.error(f"Error parsing json data: {json_data}")
            traceback.print_exc()
            return None

        logging.info(f"BuyBoxData: {str(buy_box_data)}")
        return buy_box_data
