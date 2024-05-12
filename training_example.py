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
        return f"{self.gender} shoes, type of shoes: {self.type_of_shoes}"


class ShoesView:
    @staticmethod
    def display_shoes(shoes):
        print(f"Gender: {shoes.gender}")
        print(f"Type of shoes: {shoes.type_of_shoes}")
        print(f"Color: {shoes.color}")
        print(f"Price: {shoes.price}")
        print(f"Brand: {shoes.brand}")
        print(f"Size: {shoes.size}\n")


class ShoesController:
    def __init__(self, shoes, view):
        self.shoes = shoes
        self.view = view

    def display_view(self):
        self.view.display_shoes(self.shoes)


if __name__ == "__main__":
    shoes1 = Shoes("Man", "sneakers", "black", 135, "Lonsdale", 44)
    shoes2 = Shoes("Woman", "boots", "white", 145, "Rieker", 37)
    view = ShoesView()
    controller = ShoesController(shoes1, view)
    controller.display_view()

    print(shoes1.color, shoes1.size, shoes1.type_of_shoes)
    print(shoes2)
