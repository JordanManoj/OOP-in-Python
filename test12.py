class UserAccount:
    def __init__(self, username, pin, balance=0):
        self.username = username
        self.__pin = pin
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        self.__balance = balance

    def check_pin(self, pin):
        return self.__pin == pin

class ATM:
    _instance = None

    @staticmethod
    def get_instance():
        if ATM._instance is None:
            ATM._instance = ATM()
        return ATM._instance

    def __init__(self):
        if ATM._instance is not None:
            raise Exception("This is a singleton class")
        self.logged_in_account = None
        self.accounts = {}

    def create_account(self, username, pin, balance=0):
        self.accounts[username] = UserAccount(username, pin, balance)

    def login(self, username, pin):
        if username in self.accounts and self.accounts[username].check_pin(pin):
            self.logged_in_account = self.accounts[username]
            print("Login successful!")
        else:
            print("Invalid username or pin.")

    def deposit(self, amount):
        if self.logged_in_account:
            self.logged_in_account.set_balance(self.logged_in_account.get_balance() + amount)
            print(f"Deposited Rs{amount}. New balance: Rs{self.logged_in_account.get_balance()}")
        else:
            print("Please login first.")

    def withdraw(self, amount):
        if self.logged_in_account:
            if self.logged_in_account.get_balance() >= amount:
                self.logged_in_account.set_balance(self.logged_in_account.get_balance() - amount)
                print(f"Withdrew Rs{amount}. New balance: Rs{self.logged_in_account.get_balance()}")
            else:
                print("Insufficient balance.")
        else:
            print("Please login first.")

    def check_balance(self):
        if self.logged_in_account:
            print(f"Balance: Rs{self.logged_in_account.get_balance()}")
        else:
            print("Please login first.")

atm1 = ATM.get_instance()
atm2 = ATM.get_instance()

print(atm1 is atm2)  

atm1.create_account("user1", 1234, 1000)

atm1.login("user1", 1234)
atm1.deposit(500)
atm1.withdraw(200)
atm1.check_balance()