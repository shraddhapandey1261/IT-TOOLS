class property_fun_demo:
     def __init__(self):
          self.age = 0

     @property
     def age(self):
          print("Getter method called.")
          return self._age

     @age.setter
     def age(self,age):
          if(age < 18):
               raise ValueError('Sorry your age is elow the eligibility criteria')
          print("Setter method is called")
          self._age = age

mark = property_fun_demo()

mark.age = 19
print(mark.age)
