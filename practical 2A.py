# Creating a class bank
class Bank:
    
    # Accepting user details
    user_name = str(input("Enter name:"))
    user_account_number = str(input("Enter account number:"))
    user_balance = 0
   
    # It will deposit certain amount in the bank account
    def deposit(self,deposit_amount):
        Bank.user_balance += deposit_amount
        print(f"Current balance is :{ Bank.user_balance}")
        
    # It will withdraw certain amonunt from the bank account
    def withdraw(self,withdraw_amount):
        Bank.user_balance -= withdraw_amount
        print(f"Current balance is :{ Bank.user_balance}")
 
    # Display user details     
    def user(self):
        print(f"The name is { Bank.user_name}")
        print(f'The account number is { Bank.user_account_number}')
        print(f"Curernt balance is :{ Bank.user_balance}")
        

bank_object = Bank()  # Creating an object for bank

while True:
    
    print("1.User details.")
    print("2.Deposit amount.")
    print("3.Withdraw amount")
    print("4.Quit.")
    #creating an option system to navigate through the options.
    
    option = int(input("Enter option:"))
    if option == 2:
        bank_object.deposit(int(input("Enter deposit amount:")))
    elif option ==3:
        bank_object.withdraw(int(input("Enter withdraw amount:")))
    elif option == 1:
        bank_object.user()
    elif option == 4:
        break  
