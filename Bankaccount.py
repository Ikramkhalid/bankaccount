class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: ${amount:.2f}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Holder: {self.account_holder}, Balance: ${self.balance:.2f}"


# Example usage:
# account = BankAccount("John Doe", 100.0)
# account.deposit(50)
# account.withdraw(30)
# print(account)