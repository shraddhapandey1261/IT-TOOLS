# To calculate the annual salary of employee
# Class salary for initializing the salary
class Salary:
     
     # Initializing the function
     def __init__(self,pay):
          self.pay = pay

     # Function for calculating the total pay
     def get_total(self):
          return self.pay * 12

# Class for employee salary details
class Employee(object):
     
     # Initialising the pay and bonus
     def __init__(self,pay,bonus):
          self.pay = pay
          self.bonus = bonus

     # Displaying the annual salary
     def annual_salary(self):
          return f"Total {self.pay.get_total() + self.bonus}"


object_salary = Salary(600)  # Object for taking the base pay
obj_employee = Employee(object_salary,500)  # Passing the object in the employee class to calculate the total salary
print(obj_employee.annual_salary())  # Displaying the total annual salary
