
class Salary:
     #class salary for initializing the salary
     
     def __init__(self,pay):
          self.pay = pay

     def get_total(self):
          #function for calculating the total pay
          
          return self.pay * 12

class Employee(object):
     #class for employee salary details
     
     def __init__(self,pay,bonus):
          #initialising the pay and bonus
          
          self.pay = pay
          self.bonus = bonus

     def annual_salary(self):
          #displaying the annual salary
          
          return f"Total {self.pay.get_total() + self.bonus}"

object_salary = Salary(600)                                 #object for taking the base pay
obj_employee = Employee(object_salary,500)   #passing the object in the employee class to calculate the total salary
print(obj_employee.annual_salary())                   #displaying the total annual salary
