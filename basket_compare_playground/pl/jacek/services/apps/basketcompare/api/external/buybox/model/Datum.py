import logging

from typing import Optional, Dict

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.TypeEnum import TypeEnum

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.TypeName import TypeName

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.Currency import Currency


class Datum:
    def __init__(self, data: Dict):
        self.id = data.get("id")
        self.name = data.get("name")
        # self.product_name = ""
        self.icon = data.get("icon")
        self.logo = data.get("logo")
        self.type = data.get("type")
        self.type_id = data.get("typeId")
        self.type_name = data.get("typeName")
        self.shop_id = data.get("shopId")
        self.currency = data.get("currency")
        self.price = data.get("price")
        self.price_prefix = data.get("pricePrefix")

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            # "product_name": self.product_name,
            "icon": self.icon,
            "logo": self.logo,
            "type": self.type,
            "type_id": self.type_id,
            "type_name": self.type_name,
            "shop_id": self.shop_id,
            "currency": self.currency,
            "price": self.price,
            "price_prefix": self.price_prefix
        }

    def __str__(self):
        return (f"Datum(id={self.id}, name={self.name}, "
                # f"product_name={self.product_name}, "
                f"icon={self.icon}, logo={self.logo}, "
                f"type={self.type}, type_id={self.type_id}, type_name={self.type_name}, "
                f"shop_id={self.shop_id}, currency={self.currency}, price={self.price}, "
                f"price_prefix={self.price_prefix})")

    def __repr__(self):
        return self.__str__()
