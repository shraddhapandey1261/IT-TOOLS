#To implement single inheritance

class Shape:

    
    def _get_length_breadth(self):
        #accepting input
        
        self._length=int(input("enter a number:"))
        self._breadth=int(input("enter a number:"))


class Rectangle(Shape):

    
    def calculate_area(self):
        #calculating area
        
        print("area of rectangle is", self._length * self._breadth)


obj=Rectangle()     #creating object to call the function
obj._get_length_breadth()
obj.calculate_area()
