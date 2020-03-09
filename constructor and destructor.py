#python function to find the area of rectangle using constructor and destructor

class Rectangle:


      def __init__ (self, length, breadth):
            #initializing the rectangle instance
            
            print("Initializing an rectangle instance")
            self.length=length
            self.breadth=breadth

      def area_r(self):
            #calculating the area of rectangle

            area=self.length * self.breadth
            print("Area of rectangle is ", area)

      def __del__(self):
            #destroying the instance of rectangle

            print("Instance is destroyed")


c=Rectangle(15,15)      #object being created to call the function
c.area_r()
c.__del__()
