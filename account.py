class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited ₦" + str(amount) + "." + " New balance is ₦" + str(self.balance))
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print("Withdrew ₦" + str(amount) + "." + " New balance is ₦" + str(self.balance))
        else:
            print("Invalid withdraw amount.")

    def get_balance(self):
        return self.balance

    def display(self):
        print("Account Number: " + str(self.account_number))
        print("Account Holder: " + str(self.account_holder))
        print("Balance: ₦" + str(self.balance))
