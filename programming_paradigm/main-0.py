import sys
from bank_account import BankAccount

def main():
    # Create an instance of BankAccount with an initial balance
    account = BankAccount(100)  # Example starting balance

    # Check if the user provided a command
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Parse command and amount
    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    # Process the command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
