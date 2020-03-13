#Python program
#to overload an binary + operator

class A:
     def __init__(self,a):
          self.a=a

     #adding two objwcts
     def __add__(self,o):
          return self.a+o.a

object1=A(1)
object2=A(2)
object3=A("FY")
object4=A("IT")

print(object1 + object2)
print(object3 + object4)
