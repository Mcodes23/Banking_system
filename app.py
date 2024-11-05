import uuid

def randomId():
    ''' This function returns a randomly generated UUID'''
    return str(uuid.uuid4())

class User:
    def __init__(self, userName, passWord):
        self.userName = userName
        self.passWord = passWord
        self.accounts = []
        self.is_authenticated = False  # Track authentication status

    def add_account(self, account):
        self.accounts.append(account)

    def authenticate(self, username, password):
        if self.userName == username and self.passWord == password:
            self.is_authenticated = True
            return True
        return False
    
class BankAccount:
    def __init__(self, user, id=None, initial_balance=0):
        if not user.is_authenticated:
            raise ValueError("User must be authenticated to create an account.")
        self.user = user
        self.id = id if id is not None else randomId()
        self.balance = initial_balance

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
        print(f"Account details:\n NAME: {self.user.userName}\n ID: {self.id}\n Balance: ${self.balance:.2f}")

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
    # User login and account creation with authentication
    userName = input("Enter name: ")
    userPassword = input("Enter password: ")
    user = User(userName, userPassword)

    # Authenticate the user before account creation
    entered_username = input("Authenticate - Enter your username: ")
    entered_password = input("Authenticate - Enter your password: ")
    if not user.authenticate(entered_username, entered_password):
        print("Authentication failed. Please restart the program.")
        return

    account_id = randomId()  # Generate a random UUID for the account
    account = BankAccount(user, id=account_id, initial_balance=100)  # Initial balance set by bank
    user.add_account(account)

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
                account.withdraw(userWithdraw)
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '3':
            account.displayDetails()

        elif choice == '4':
            print("Thank you for transacting with us")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
