from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.BuyBoxData import BuyBoxData


class BuyBoxResponse:
    buy_box_data: BuyBoxData

    def __init__(self, buy_box_data: BuyBoxData):
        self.buy_box_data = buy_box_data

    def __str__(self) -> str:
        return f"BuyBoxResponse(data={self.buy_box_data})"
