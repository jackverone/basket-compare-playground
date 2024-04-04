import logging

from typing import Optional, Dict

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.TypeEnum import TypeEnum

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.TypeName import TypeName

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.Currency import Currency


class Datum:
    def __init__(self, data: Dict):
        self.id = data.get('id')
        self.name = data.get('name')
        self.icon = data.get('icon')
        self.logo = data.get('logo')
        self.type = data.get('type')
        self.type_id = data.get('typeId')
        self.type_name = data.get('typeName')
        self.shop_id = data.get('shopId')
        self.currency = data.get('currency')
        self.price = data.get('price')
        self.price_prefix = data.get('pricePrefix')

    # id: int
    # name: str
    # icon: str
    # logo: str
    # type: TypeEnum
    # type_id: int
    # type_name: TypeName
    # shop_id: int
    # currency: Currency
    # price: str
    # price_prefix: Optional[str]
    #
    # def __init__(self, json_data):
    #     if json_data is None:
    #         logging.error("Datum: json_data is None")
    #         json_data = {}
    #
    #     self.id = json_data.get("id")
    #     self.name = json_data.get("name")
    #     self.icon = json_data.get("icon")
    #     self.logo = json_data.get("logo")
    #     self.type = TypeEnum(json_data.get("type", {}))
    #     self.type_id = json_data.get("typeId")
    #     self.type_name = TypeName(json_data.get("typeName", {}))
    #     self.shop_id = json_data.get("shopId")
    #     self.currency = Currency(json_data.get("currency", {}))
    #     self.price = json_data.get("price")
    #     self.price_prefix = json_data.get("pricePrefix")

    def __str__(self):
        return (f"Datum(id={self.id}, name={self.name}, icon={self.icon}, logo={self.logo}, type={self.type}, "
                f"type_id={self.type_id}, type_name={self.type_name}, shop_id={self.shop_id}, currency={self.currency},"
                f" price={self.price}, price_prefix={self.price_prefix})")
