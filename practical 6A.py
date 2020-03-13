#class animal created
class Animal:

    def speak(self):  

        print("Animal Speaking")  


#child class Dog inherits the base class Animal  
class Dog(Animal):
  
    def bark(self):  

        print("dog barking")  

        
#objects for animals
dog_object = Dog()  
dog_object.bark()  
dog_object.speak()  
