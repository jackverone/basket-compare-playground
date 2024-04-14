class BasketCompareService:
    def __init__(self, repository):
        self.repository = repository

    def create_basket_compare(self):
        return self.repository.create_basket_compare()

    def get_basket_compare(self, id):
        return self.repository.get_basket_compare(id)

    def delete_basket_compare(self, id):
        return self.repository.delete_basket_compare(id)
