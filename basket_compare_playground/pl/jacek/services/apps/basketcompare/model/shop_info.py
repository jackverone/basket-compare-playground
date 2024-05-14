class ShopInfo:

    def __init__(self, id: str, name: str, product_image_url: str = None, icon_url: str = None):
        self.id = id
        self.name = name
        self.product_image_url = product_image_url
        self.icon_url = icon_url

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.product_image_url,
            "icon_url": self.icon_url
        }

    def __str__(self):
        return (f"shop_id={self.id}, shop_name={self.name}, "
                f"shop_url={self.product_image_url}, shop_logo_url={self.icon_url}")

    def __repr__(self):
        return self.__str__()
