from basket_compare_playground.pl.jacek.services.apps.basketcompare.model.product_meta_data import ProductMetaData


class Product:

    def __init__(self, id, name, icon, logo, type, type_id, type_name, shop_id, currency, price: float,
                 price_prefix, product_meta_data: ProductMetaData = None,
                 product_name: str = "", product_info: str = "", product_url: str = ""):
        self.id = id
        self.name = name
        self.icon = icon
        self.logo = logo
        self.type = type
        self.type_id = type_id
        self.type_name = type_name
        self.shop_id = shop_id
        self.currency = currency
        self.price = price
        self.price_prefix = price_prefix
        self.product_meta_data = product_meta_data
        self.product_name = product_name
        self.product_info = product_info
        self.product_url = product_url

    # @property
    # def product_meta_data(self):
    #     return self.product_meta_data
    #
    # @product_meta_data.setter
    # def product_meta_data(self, value):
    #     self.product_meta_data = value
    #
    # @property
    # def product_url(self):
    #     return self.product_url
    #
    # @product_url.setter
    # def product_url(self, product_url):
    #     self.product_url = product_url

    def __dict__(self):
        return {
            "id": self.id,
            "name": self.name,
            "icon": self.icon,
            "logo": self.logo,
            "type": self.type,
            "type_id": self.type_id,
            "type_name": self.type_name,
            "shop_id": self.shop_id,
            "currency": self.currency,
            "price": self.price,
            "price_prefix": self.price_prefix,
            "product_name": self.product_name,
            "product_info": self.product_info,
            "product_url": self.product_url
        }

    def to_dict(self):
        return self.__dict__()

    def __str__(self):
        return (f"Product(id={self.id}, name={self.name}, icon={self.icon}, logo={self.logo}, type={self.type}, "
                f"type_id={self.type_id}, type_name={self.type_name}, shop_id={self.shop_id}, "
                f"currency={self.currency}, price={self.price}, price_prefix={self.price_prefix}, "
                f"product_name={self.product_name}, product_info={self.product_info}, product_url={self.product_url})")

    def __repr__(self):
        return self.__str__()
