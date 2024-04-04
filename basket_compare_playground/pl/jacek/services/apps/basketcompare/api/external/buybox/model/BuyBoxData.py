import logging

from typing import Dict, List

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.Datum import Datum

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.Statistics import \
    Statistics


from typing import Dict, Optional


class BuyBoxData:
    def __init__(self, json_data: Dict):
        logging.info(f"BuyBoxData: json_data={json_data}")

        self.status = json_data.get('status')
        if isinstance(json_data.get('data'), dict):
            self.data = {k: Datum(v) for k, v in json_data.get('data', {}).items()}
        self.space_id = json_data.get('spaceId')
        self.tracking_url = json_data.get('trackingUrl')
        self.sort_type = json_data.get('sortType')
        self.use_css = json_data.get('useCSS')
        self.use_tabs = json_data.get('useTabs')
        self.default_tab = json_data.get('defaultTab')
        self.lead_color = json_data.get('leadColor')
        self.show_product = json_data.get('showProduct')
        self.shop_style = json_data.get('shopStyle')
        self.version = json_data.get('version')
        self.language = json_data.get('language')
        self.show_prices = json_data.get('showPrices')
        self.send_ga_client_id = json_data.get('sendGaClientId')
        self.button_label = json_data.get('buttonLabel')
        self.row_count = json_data.get('rowCount')
        self.statistics = Statistics(json_data.get('statistics', {}))
        self.name = json_data.get('name')
        self.info = json_data.get('info')
        self.image = json_data.get('image')

    def sort_data_by_price(self):
        if hasattr(self, 'data'):
            self.data = dict(sorted(self.data.items(), key=lambda item: float(item[1].price)))

    def __str__(self):
        data_str = ''
        if hasattr(self, 'data'):
            data_str = ', '.join(f"{k}: {str(v)}" for k, v in self.data.items())
        return (f"BuyBoxData(status={self.status}, data={{{data_str}}}, space_id={self.space_id}, "
                f"tracking_url={self.tracking_url}, sort_type={self.sort_type}, use_css={self.use_css}, "
                f"use_tabs={self.use_tabs}, default_tab={self.default_tab}, lead_color={self.lead_color}, "
                f"show_product={self.show_product}, shop_style={self.shop_style}, version={self.version}, "
                f"language={self.language}, show_prices={self.show_prices}, send_ga_client_id={self.send_ga_client_id},"
                f" button_label={self.button_label}, row_count={self.row_count}, statistics={self.statistics}, "
                f"name={self.name}, info={self.info}, image={self.image})")
