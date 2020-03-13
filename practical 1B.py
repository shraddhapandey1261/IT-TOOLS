# Creating class to implement arithmetic operations
class Arithmetic_oprt:

    # Function to calculate arithmetic operations
    def calculations(self,number1,number2):
        print(f"The addition of the numbers is :{number1 + number2}")
        print(f"The subtraction of the numbers is :{number1 - number2}")
        print(f"The multiplication of the numbers is :{number1 * number2}")
        print(f"The division of the numbers is :{number1 / number2}")
        print(f"The modulus division of the numbers is:{number1 %number2}")
        print(f"The value of number 1 raised to number2 is {number1 ** number2}")
        print(f"The value of integer division of the numbers is {number1 // number2}")

a1 = Arithmetic_oprt()  # Creating an instance
a1.calculations(int(input("Enter number1:")),int(input("Enter number2:")))
