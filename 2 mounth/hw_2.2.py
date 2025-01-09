class Figure:
    unit = "cm"
    def __init__(self):
        pass
    def calculate_area(self):
        pass
    def info(self):
        pass

class Square(Figure):
    def __init__(self, side_lenght):
        super().__init__()
        self.__side_lenght = side_lenght

    def calculate_area(self ):
        square = self.__side_lenght ** 2
        return square

    def info(self):
        print(f"Square side length: {self.__side_lenght}{self.unit}, area: {self.calculate_area()}{self.unit}")

class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        rectangle = self.__width * self.__length
        return rectangle

    def info(self):
        print(f"Rectangle length: {self.__length}, width: {self.__width}, area: {self.calculate_area()}{self.unit}")


square1 = Square(3)
square2 = Square(5)

rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(2, 3)
rectangle3 = Rectangle(3, 9)

list_figure = [square1, square2, rectangle1, rectangle2, rectangle3]
for figure in list_figure:
    figure.info()
