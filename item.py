class Item: 
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
        pass

    def create_dict_obj(self):
        return {
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
            }

