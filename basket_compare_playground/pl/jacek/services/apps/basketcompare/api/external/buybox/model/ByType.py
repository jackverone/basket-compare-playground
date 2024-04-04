import logging
from typing import Dict

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.Book import Book


class ByType:
    def __init__(self, data: Dict):
        self.audiobook = Book(data.get('audiobook', {}))
        self.ebook = Book(data.get('ebook', {}))
        self.book = Book(data.get('book', {}))

    # audiobook: Book
    # book: Book
    # ebook: Book
    #
    # def __init__(self, json_data):
    #     if json_data is None:
    #         logging.error("ByType: json_data is None")
    #         json_data = {}
    #
    #     self.audiobook = Book(json_data.get("audiobook", {}))
    #     self.book = Book(json_data.get("book", {}))
    #     self.ebook = Book(json_data.get("ebook", {}))

    def __str__(self):
        return f"ByType(audiobook={self.audiobook}, book={self.book}, ebook={self.ebook})"
