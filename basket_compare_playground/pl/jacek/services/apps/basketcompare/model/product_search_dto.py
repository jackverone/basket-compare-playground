class ProductSearchDto:
    def __init__(self, name, info, id: int = None, type: str = None, type_id: int = None):
        self.name = name
        self.info = info
        self.id = id
        self.type = type
        self.type_id = type_id

    def __str__(self):
        return (f"ProductSearchDto(name={self.name}, info={self.info}, id={self.id}, type={self.type}, "
                f"type_id={self.type_id})")

    def __repr__(self):
        return self.__str__()
