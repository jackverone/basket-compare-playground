from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product import Product

from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.shop_info import ShopInfo


def from_product(product: Product) -> ShopInfo:
    shop_info = ShopInfo(
        product.id,
        product.name,
        product.product_meta_data.image,
        product.icon
    )
    return shop_info
