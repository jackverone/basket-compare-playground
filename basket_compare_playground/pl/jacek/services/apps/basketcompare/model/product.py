
class Product:
    def __init__(self, name, price, shop_id):
        self.name = name
        self.price = price
        self.shop_id = shop_id

    def __dict__(self):
        return {
            'name': self.name,
            'price': self.price,
            'shop_id': self.shop_id
        }

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'shop_id': self.shop_id
        }
