class Parent:
    #creating parent class

    def func1(self):
        print("This is function one")

class Child(Parent):
    def func2(self):
        print("This is function two")

class Child1(Parent):
    def func3(self):
        print("This is function three")

class Child3(Child,Child1):
    def func4(Self):
        print("This is function four")

obj=Child3()
obj.func2()
