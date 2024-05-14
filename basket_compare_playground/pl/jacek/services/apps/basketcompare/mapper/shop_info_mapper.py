import logging

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product import Product

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.shop_info import ShopInfo


def map_shop_info_from_product(product: Product) -> ShopInfo:
    # logging.info(f"map_shop_info_from_product(product)")
    shop_info = ShopInfo(
        product.id,
        product.name,
        product.product_meta_data.image,
        product.icon
    )
    # logging.info(f"map_shop_info_from_product(...) = shop_info")
    return shop_info
