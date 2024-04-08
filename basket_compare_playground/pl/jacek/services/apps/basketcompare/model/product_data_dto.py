from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.BuyBoxData import BuyBoxData


class ProductDataDto:
    """
    Class to store product data, used as wrapper
    for BuyBoxData class which is BuyBox API model.
    """

    def __init__(self):
        self.product_data = None

    def convert_buybox_to_dto(self, buybox_data: BuyBoxData):
        self.product_data = buybox_data

    def __str__(self):
        return f"ProductDataDto(product_data={self.product_data})"
