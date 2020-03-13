#python function to fing the area of rectangle using constructor and destructor

class Rectangle:

      #initializing the rectangle instance

      def __init__ (self,l,b):
           print("Initializing an rectangle instance")
           self.l=l
           self.b=b

      #calculating the area of rectangle
           
      def area_r(self):
            area=self.l*self.b
            print("Area of rectangle is ",area)

      #destroying the instance of rectangle

      def __del__(self):
         print("Instance is destroyed")

c=Rectangle(15,15)
c.area_r()
c.__del__()
