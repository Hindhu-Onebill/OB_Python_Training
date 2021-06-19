class Rectangle:

    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def areaOfRectangle(self):
        return self.lenght * self.width


lenght = int(input("enter the length:"))
width = int(input("enter the width:"))
res = Rectangle(lenght, width)
print(res.areaOfRectangle())
