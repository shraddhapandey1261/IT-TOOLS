#Python program showing a use of property() function

class Property_function_demo:

     
     def __init__(self):
          #function to initialize the age attribute

          self._age=0
          
     def get_age(self):
          #function to get value of _age

          print("Getter method called")
          return self._age
     
     def set_age(self, a):
          #function to set value of _age

          print("Setter method called")
          self._age=a
          
     def del_age(self):
          #function to delete _age attribute

          del self._age

     age=property(get_age, set_age, del_age)      #using property() function

     
mark=Property_function_demo()      #object being created to call the function
mark.age=10
print(mark.age)
        
