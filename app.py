import random
def randomId():
    ''' This function returns a random number between 10,000 and 99,999'''
    randomNumber = random.randint(10000, 99999)
    return randomNumber



class BankAccount(object):
    def __init__(self, name, balance, id = None):
        self.name = name #Initializing the name attribute
        self.id =  id if id is not None else randomId() #Initializing the number attribute
        self.balance = balance #Initializing the balance attribute

        #class methods
    def deposit(self, depositAmount):
        if depositAmount <= 0:
            raise ValueError("Value must be positive")
        self.balance += depositAmount  # balance update


    def withdraw(self, withdrawAmount):
        if withdrawAmount <= 0:
            raise ValueError("Value must be positive")
        if self.balance < withdrawAmount:
            print("Please make a lesser withdrawal")
        else:
            self.balance -= withdrawAmount  # balance update


    def displayDetails(self):
        print(f"Account details:\n NAME: {self.name}\n ID: {self.id}\n Balance: ${self.balance:.2f}")
        

class SavingsAccount(BankAccount):
    def __init__(self, name, balance, minimum_balance, id=None):
        super().__init__(name, balance, id)  # constructor of the parent class
        self.minimum_balance = minimum_balance  # minimum balance for the savings account

    def withdraw(self, withdrawAmount):
        if withdrawAmount <= 0:
            raise ValueError("Value must be positive")
        # if balance after withdrawal
        if self.balance - withdrawAmount < self.minimum_balance:
            print(f"Withdrawal denied. Balance cannot fall below the minimum balance of ${self.minimum_balance}.")
        else:
            self.balance -= withdrawAmount  # balance update


class CheckingAccount(BankAccount):
    def __init__(self, name, balance, checkbook_issued=False, id=None):
        super().__init__(name, balance, id)
        self.checkbook_issued = checkbook_issued  # issued checkbook

    def issue_checkbook(self):
        if self.checkbook_issued:
            print("Checkbook has already been issued. Only one checkbook can be issued per account.")
        else:
            self.checkbook_issued = True
            print("Checkbook has been issued.")

    def withdraw(self, withdrawAmount):
        if withdrawAmount <= 0:
            raise ValueError("Value must be positive")
        # Allow overdraft, for example, up to $100 below the balance
        overdraft_limit = 100
        if self.balance + overdraft_limit < withdrawAmount:
            print("Withdrawal denied. Insufficient funds.")
        else:
            self.balance -= withdrawAmount  # Update balance

    def displayDetails(self):
        super().displayDetails()  # Call the parent class method
        checkbook_status = "Yes" if self.checkbook_issued else "No"
        print(f"Checkbook Issued: {checkbook_status}")

# Function to get a valid float input
def get_valid_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Value must be non-negative.")
            return value
        except ValueError as e:
            print(e)  # Print the error message


# Creating a BankAccount instance with error handling for user input
name = input("Enter name: ")
account_id = "001"
initial_balance = get_valid_float("Enter initial balance: ")
account = BankAccount(name=name, id=account_id, balance=initial_balance)

# Deposit and withdraw with error handling
try:
    userDeposit = get_valid_float("Amount to deposit: ")
    account.deposit(userDeposit)
    
    userWithdraw = get_valid_float("Amount to withdraw: ")
    account.withdraw(userWithdraw)

    account.displayDetails()
except ValueError as e:
    print(f"Error: {e}")

