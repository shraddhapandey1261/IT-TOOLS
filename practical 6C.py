# Father class created
class Father:
    fathername = ""
 
    def show_father(self):
        print(self.fathername)
 
 
# Mother class created
class Mother:
    mothername = ""
 
    def show_mother(self):
        print(self.mothername)
 
 
# Son class inherits Father and Mother classes
class Son(Father, Mother):
    def show_parent(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
 
son_object = Son()  # Object of Son class
son_object.fathername = "Mark"
son_object.mothername = "Sonia"
son_object.show_parent()
