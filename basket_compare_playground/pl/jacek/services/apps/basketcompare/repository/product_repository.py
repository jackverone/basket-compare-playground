class ProductRepository:
    def __init__(self):
        self.products = []

    def create_product(self, name, price):
        # product = Product(name, price)
        # self.products.append(product)
        # return product
        pass

    def get_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

    def update_product(self, name, price):
        product = self.get_product(name)
        if product:
            product.price = price
            return product
        return None

    def delete_product(self, name):
        product = self.get_product(name)
        if product:
            self.products.remove(product)
            return True
        return False
