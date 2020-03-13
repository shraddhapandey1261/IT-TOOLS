#python program to perform addition
#of two complex numbers using binary
#+ operator overloading

class complex:
     def __init__(self,a,b):
          self.a=a
          self.b=b

     #adding two objects
     def __add__(self,other):
          return self.a+other.a,self.b+other.b

     def __str__(self):
          return self.a,self.b

Object1=complex(1,2)
Object2=complex(2,3)
Object3=Object1+Object2

print(Object3)
