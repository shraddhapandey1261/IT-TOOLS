#Python program to overload
# a comparison operators

class A:
     def __init__(self,a):
          self.a=a

     def __gt__(self,other):
          if(self.a>other.a):
               return True
          else:
               return False
object1=A(2)
object2=A(3)
if(object1>object2):
     print("object1 is greater than object2")
else:
     print("object2 is greater than object1")
