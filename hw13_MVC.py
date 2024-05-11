class Shoes:
    """Model"""
    def __init__(self, gender, type_of_shoes, color, price, brand, size):
        self.gender = gender
        self.type_of_shoes = type_of_shoes
        self.color = color
        self.price = price
        self.brand = brand
        self.size = size

    def __str__(self):
        return f"{self.gender} shoes, type of shoes: {self.type_of_shoe}"


class ShoesView:
    @staticmethod
    def display_shoes(shoes):
        print(f"Gender: {shoes.gender}")
        print(f"Type of shoes: {shoes.type_of_shoes}")
        print(f"Color: {shoes.color}")
        print(f"Price: {shoes.price}")
        print(f"Brand: {shoes.brand}")
        print(f"Size: {shoes.size}")


class ShoesControler:
    def __int__(self):
