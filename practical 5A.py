class property_function_demo:
     #class property function created
     
     def __init__(self):
          
          self._age = 0

     def get_age(self):
          #fucntion for printing the age
          
          print("Getter method called")
          return self._age

     def set_age(self,age):
          #function for setting the age
          
          print("setter method called")

     def delete_age(self):
          #function for deleting the age
          del self.age

     age = property(get_age,set_age)

object1 = property_function_demo()
object1.age = 10
print(object1.age)
