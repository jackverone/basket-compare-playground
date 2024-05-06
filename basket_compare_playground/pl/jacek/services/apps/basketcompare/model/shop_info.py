class ShopInfo:

    def __init__(self, shop_id: str, shop_name: str, shop_url: str = None, shop_icon_url: str = None):
        self.shop_id = shop_id
        self.shop_name = shop_name
        self.shop_url = shop_url
        self.shop_icon_url = shop_icon_url

    def to_dict(self):
        return {
            "shop_id": self.shop_id,
            "shop_name": self.shop_name,
            "shop_url": self.shop_url,
            "shop_icon_url": self.shop_icon_url
        }

    def __str__(self):
        return (f"shop_id={self.shop_id}, shop_name={self.shop_name}, shop_url={self.shop_url}, "
                f"shop_logo_url={self.shop_icon_url}")

    def __repr__(self):
        return self.__str__()
