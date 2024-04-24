import logging
from typing import Dict

from basket_compare_playground.pl.jacek.services.apps.basketcompare.api.external.buybox.model.Book import Book


class ByType:
    def __init__(self, data: Dict):
        self.audiobook = Book(data.get("audiobook", {}))
        self.ebook = Book(data.get("ebook", {}))
        self.book = Book(data.get("book", {}))

    def to_dict(self) -> Dict:
        return {
            "audiobook": self.audiobook.to_dict(),
            "ebook": self.ebook.to_dict(),
            "book": self.book.to_dict()
        }

    def __str__(self):
        return f"ByType(audiobook={self.audiobook}, book={self.book}, ebook={self.ebook})"
