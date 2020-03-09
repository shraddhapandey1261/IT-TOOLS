class Employee:
     #class employee created


     def add(self,salary,incentive):
          #function to calculate salary and incentive.

          print(f"Total salary of the base class is {salary + incentive}.")


class Department(Employee):
     #class department created


     temp = "I am a member of the department class."
     def add(self,salary,incentive):
          #function to calculate salary and incentive.

          print(f"Total salary of the derived class is {salary + incentive}.")
          super(Department,self).add(salary,incentive)


#class objects created.
          
dept = Department()
dept.add(45000,5000)
