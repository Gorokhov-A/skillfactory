class Rectangle:

    def __init__(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def attrib_set(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        return (f'Rectangle ({self.x},{self.y},{self.width},{self.height})')

rectangle = Rectangle()
print(rectangle.attrib_set(5, 10, 50, 100))