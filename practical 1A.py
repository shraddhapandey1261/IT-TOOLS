import math

class Rectangle:
    def calculation(self,length,breadth):
        print(f"Area of the rectangle is {length * breadth}")

class Square:
    def calculation(self,side):
        print(f"The area of the square is {side ** 2}")

class Circle:
    def calculation(self,radius):
        print(f"The area of the circle is {math.pi * radius ** 2}")
    
class Ellipse:
    def calculation(self,x_axis,y_axis):
        print(f"The area of the Ellipse is {math.pi * x_axis * y_axis}")

a1 = Rectangle()
a2 = Square()
a3 = Circle()
a4 = Ellipse()

while True:
    print("1.Area of the rectangle.")
    print("2.Area of the Square.")
    print("3.Area of the Circle.")
    print("4.Area of the Ellipse.")
    print("5.Quit")
    opt = int(input("Enter option:"))
    if opt == 1:
        a1.calculation(int(input("Enter length")),int(input("Enter breadth")))
    elif opt == 2:
        a2.calculation(int(input("Enter side")))
    elif opt == 3:
        a3.calculation(int(input("Enter radius")))
    elif opt == 4:
        a4.calculation(int(input("Enter x_axis")),int(input("Enter y_axis")))
    else:
        break