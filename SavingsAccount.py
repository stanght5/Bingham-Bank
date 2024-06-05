from account import Account


class SavingsAccount(Account):
    def __init__(self, account_number, account_holder, balance=0):
        super().__init__(account_number, account_holder, balance)
        self.__interest_rate = 0.5 / 100

    def get_interest_rate(self):
        return self.__interest_rate * 100

    def set_interest_rate(self, interest_rate):
        self.__interest_rate = interest_rate / 100
        return self.__interest_rate * 100

    def deposit(self, amount):
        super().deposit(amount)

    def withdraw(self, amount):
        if amount > 700000:
            print("withdrawal limit exceeded")
        else:
            super().withdraw(amount)

    def add_interest(self):
        interest_rate = self.get_interest_rate()
        interest = self.balance * interest_rate
        self.deposit(interest)
        return interest


savings = SavingsAccount(823948388, "kevin mathias", 2000)
savings.deposit(1000)
savings.withdraw(500)
savings.withdraw(800000)
savings.add_interest()
savings.display()
