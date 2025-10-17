
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rs{amount:.2f}. New balance: Rs{self.balance:.2f}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew Rs{amount:.2f}. New balance: Rs{self.balance:.2f}")

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: Rs{self.balance:.2f}")

account = BankAccount("Josh MC", 3700)
account.display_balance()
account.deposit(500)
account.withdraw(200)
account.withdraw(2000)
account.display_balance()