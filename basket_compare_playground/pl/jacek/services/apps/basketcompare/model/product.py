class Product:

    def __init__(self, id, name, product_name, icon, logo, type, type_id, type_name, shop_id, currency, price,
                 price_prefix):
        self.id = id
        self.name = name
        self.product_name = product_name
        self.icon = icon
        self.logo = logo
        self.type = type
        self.type_id = type_id
        self.type_name = type_name
        self.shop_id = shop_id
        self.currency = currency
        self.price = price
        self.price_prefix = price_prefix

    def __dict__(self):
        return {
            "id": self.id,
            "name": self.name,
            "product_name": self.product_name,
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

    def to_dict(self):
        return self.__dict__()

    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, product_name={self.product_name}, icon={self.icon}, " \
               f"logo={self.logo}, type={self.type}, type_id={self.type_id}, type_name={self.type_name}, " \
               f"shop_id={self.shop_id}, currency={self.currency}, price={self.price}, price_prefix={self.price_prefix})"

    def __repr__(self):
        return self.__str__()
