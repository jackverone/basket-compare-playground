import traceback
import logging
import requests
import json

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.BuyBoxResponse import \
    BuyBoxResponse
from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.BuyBoxData import BuyBoxData


class BuyBoxService:
    def __init__(self, base_url="https://buybox.click"):
        self.base_url = base_url

    def get_buybox(self, bb_id, name, name_value, info, info_value):
        logging.info(f"Getting buybox with {bb_id} for {name}={name_value}")

        url = f"{self.base_url}/{bb_id}/buybox.json?{name}={name_value}&{info}={info_value}"
        response = requests.get(url)

        logging.info(f"response: {response}")
        return response

    def get_buybox_by_name(self, name_value, info_value):
        return self.get_buybox("17970", "name", name_value, "info", info_value)

    def get_buybox_result(self, name_value, info_value):
        logging.info(f"Getting buybox result for {name_value} and {info_value}")

        # json_data = dict()
        try:
            json_data = self.get_buybox_by_name(name_value, info_value)
            parsed_json = json.loads(json_data.text)
            logging.info(f"parsed_json: {parsed_json}")
            buy_box_data = BuyBoxData(parsed_json)
            buy_box_data.sort_data_by_price()

            # logging.info(f"TYPE: {type(buy_box_data)}")
            logging.info(f"BuyBoxData: {str(buy_box_data)}")
            # buy_box_data.buy_box_data.sort_data_by_price()
        except TypeError as e:
            logging.error(f"Error parsing json data: {json_data}")
            traceback.print_exc()
            return None

        logging.info(f"BuyBoxData: {str(buy_box_data)}")
        return buy_box_data
