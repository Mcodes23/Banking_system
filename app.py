import uuid

def randomId():
    ''' This function returns a randomly generated UUID'''
    return str(uuid.uuid4())

class BankAccount(object):
    def __init__(self, name, balance, id=None):
        self.name = name  # Initializing the name attribute
        self.id = id if id is not None else randomId()  # Initializing the ID attribute
        self.balance = balance  # Initializing the balance attribute

    def deposit(self, depositAmount):
        if depositAmount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += depositAmount  # Update balance

    def withdraw(self, withdrawAmount):
        if withdrawAmount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if self.balance < withdrawAmount:
            print("Insufficient funds: Please make a lesser withdrawal.")
        else:
            self.balance -= withdrawAmount  # Update balance
            print(f"Withdrawal successful: ${withdrawAmount:.2f}")

    def displayDetails(self):
        print(f"Account details:\n NAME: {self.name}\n ID: {self.id}\n Balance: ${self.balance:.2f}")

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

def main():
    # Creating a BankAccount instance with error handling for user input
    name = input("Enter name: ")
    account_id = randomId()  # Generate a random UUID
    initial_balance = get_valid_float("Enter initial balance: ")
    account = BankAccount(name=name, id=account_id, balance=initial_balance)

    while True:
        print("\nOptions:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            try:
                userDeposit = get_valid_float("Amount to deposit: ")
                account.deposit(userDeposit)
                print(f"Deposited: ${userDeposit:.2f}")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            try:
                userWithdraw = get_valid_float("Amount to withdraw: ")
                account.withdraw(userWithdraw)  # Process withdrawal
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '3':
            account.displayDetails()

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
