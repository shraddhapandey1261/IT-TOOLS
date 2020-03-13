#Python program to overload equality
# and less thean operator

class A:
     def __init__(self,a):
          self.a=a

     def __lt__(self,other):
          if(self.a<other.a):
               return "object1 is less than object2"
          else:
               return "object2 is less than object1"

     def __eq__(self,other):
          if(self.a==other.a):
               return "Both are equal"
          else:
               return "Not equal"
          
object1=A(2)
object2=A(3)
print(object1<object2)

object3=A(4)
object4=A(4)
print(object1==object2)
