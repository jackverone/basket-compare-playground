class Product:

    def __init__(self, name, icon, logo, type, type_id, type_name, shop_id, currency, price,
                 price_prefix, product_name=""):
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
        self.product_name = product_name
        self.product_meta_data = None

    def add_product_meta_data(self, product_meta_data):
        self.product_meta_data = product_meta_data

    def __dict__(self):
        return {
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
            "product_name": self.product_name
        }

    def to_dict(self):
        return self.__dict__()

    def __str__(self):
        return (f"Product(name={self.name}, icon={self.icon}, logo={self.logo}, type={self.type}, "
                f"type_id={self.type_id}, type_name={self.type_name}, shop_id={self.shop_id}, "
                f"currency={self.currency}, price={self.price}, price_prefix={self.price_prefix}, "
                f"product_name={self.product_name}, product_meta_data={self.product_meta_data})")

    def __repr__(self):
        return self.__str__()
