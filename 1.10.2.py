class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


rectangle = Rectangle(50,100)

print("Площадь прямоугольника=",rectangle.get_area())

