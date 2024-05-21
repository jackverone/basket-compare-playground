import logging

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model import BuyBoxData
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_meta_data import ProductMetaData


def extract_product_meta_data(buybox_data: BuyBoxData) -> ProductMetaData:
    logging.info(f"extract_product_meta_data(buybox_data)")
    if not hasattr(buybox_data, "data"):
        return None

    product_meta_data = ProductMetaData(
        buybox_data.status,
        buybox_data.space_id,
        buybox_data.tracking_url,
        buybox_data.sort_type,
        buybox_data.use_css,
        buybox_data.use_tabs,
        buybox_data.default_tab,
        buybox_data.lead_color,
        buybox_data.show_product,
        buybox_data.shop_style,
        buybox_data.version,
        buybox_data.language,
        buybox_data.show_prices,
        buybox_data.send_ga_client_id,
        buybox_data.button_label,
        buybox_data.row_count,
        buybox_data.statistics,
        buybox_data.name,
        buybox_data.info,
        buybox_data.image
    )
    # logging.info(f"extract_product_meta_data(...) = product_meta_data")
    return product_meta_data
