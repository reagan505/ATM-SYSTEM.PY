class Account:
    def __init__(self, name, balance=0.0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"KES {amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"KES {amount} withdrawn successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Your current balance is: KES {self.balance}")

def main():
    print("Welcome to NATACK ATM")
    account = None

    while True:
        print("\n1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            if account is None:
                name = input("Please enter your name: ")
                try:
                    initial_balance = float(input("Please enter your initial balance: "))
                    if initial_balance < 0:
                        print("Initial balance cannot be negative.")
                    else:
                        account = Account(name, initial_balance)
                        print("Account created successfully!")
                except ValueError:
                    print("Invalid input for initial balance. Please enter a number.")
            else:
                print("Account already exists.")

        elif choice == '2':
            if account:
                try:
                    amount = float(input("Enter deposit amount: "))
                    account.deposit(amount)
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("Please create an account first.")

        elif choice == '3':
            if account:
                try:
                    amount = float(input("Enter withdrawal amount: "))
                    account.withdraw(amount)
                except ValueError:
                    print("Invalid input. Please enter a number.")
            else:
                print("Please create an account first.")

        elif choice == '4':
            if account:
                account.check_balance()
            else:
                print("Please create an account first.")

        elif choice == '5':
            print("Thank you for using Python ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
