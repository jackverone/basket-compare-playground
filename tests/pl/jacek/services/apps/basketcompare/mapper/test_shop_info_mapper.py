from unittest import TestCase

from basket_compare_playground.pl.jacek.services.apps.basketcompare.mapper.shop_info_mapper import map_shop_info_from_product
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product import Product
from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_meta_data import ProductMetaData


class Test(TestCase):
    def test_from_product(self):
        # Given
        product_meta_data: ProductMetaData = ProductMetaData(
            status="status",
            space_id="space_id",
            tracking_url="tracking_url",
            sort_type="sort_type",
            use_css="use_css",
            use_tabs="use_tabs",
            default_tab="default_tab",
            lead_color="lead_color",
            show_product="show_product",
            shop_style="shop_style",
            version="version",
            language="language",
            show_prices="show_prices",
            send_ga_client_id="send_ga_client_id",
            button_label="button_label",
            row_count="row_count",
            statistics="statistics",
            name="name",
            info="info",
            image="http://images.com/image.png"
        )

        product: Product = Product(
            id=128049855,
            name="shop.com",
            icon="http://icons.com/shop.png",
            logo="logo",
            type="book",
            type_id="type_id",
            type_name="type_name",
            shop_id="shop_id",
            currency="currency",
            price="price",
            price_prefix="price_prefix",
            product_meta_data=product_meta_data,
            product_name="product_name",
            product_url="product_url"
        )

        # When
        shop_info = map_shop_info_from_product(product)

        # Then
        self.assertEqual(shop_info.id, product.id)
        self.assertEqual(shop_info.name, product.name)
        self.assertEqual(shop_info.icon_url, product.icon)
