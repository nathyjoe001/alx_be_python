class BankAccount:
    def __init__(self, initial_balance=0):
        """
        Initialize the BankAccount with an optional initial balance (default: 0).
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit a specified amount into the account.
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw a specified amount from the account if funds are sufficient.
        Returns True if the withdrawal was successful, otherwise False.
        """
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """
        Display the current balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
