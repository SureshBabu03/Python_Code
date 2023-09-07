class ATM:
    def __init__(self):
        self.accounts = {}  # Dictionary to store account numbers and balances

    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = initial_balance
            return f"Account {account_number} created with an initial balance of ${initial_balance}"
        else:
            return f"Account {account_number} already exists."

    def check_balance(self, account_number):
        if account_number in self.accounts:
            return f"Account {account_number} balance: ${self.accounts[account_number]}"
        else:
            return "Account not found."

    def deposit(self, account_number, amount):
        if account_number in self.accounts and amount > 0:
            self.accounts[account_number] += amount
            return f"Deposited ${amount} into account {account_number}. New balance: ${self.accounts[account_number]}"
        elif account_number not in self.accounts:
            return "Account not found."
        else:
            return "Invalid deposit amount."

    def withdraw(self, account_number, amount):
        if account_number in self.accounts and amount > 0:
            if amount <= self.accounts[account_number]:
                self.accounts[account_number] -= amount
                return f"Withdrew ${amount} from account {account_number}. New balance: ${self.accounts[account_number]}"
            else:
                return "Insufficient funds."
        elif account_number not in self.accounts:
            return "Account not found."
        else:
            return "Invalid withdrawal amount."

def main():
    atm = ATM()

    while True:
        print("\nATM Menu:")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            initial_balance = float(input("Enter initial balance: $"))
            print(atm.create_account(account_number, initial_balance))
        elif choice == '2':
            account_number = input("Enter account number: ")
            print(atm.check_balance(account_number))
        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter the deposit amount: $"))
            print(atm.deposit(account_number, amount))
        elif choice == '4':
            account_number = input("Enter account number: ")
            amount = float(input("Enter the withdrawal amount: $"))
            print(atm.withdraw(account_number, amount))
        elif choice == '5':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
