from account import Account

class Children_Account(Account):
    def __init__(self, account_number, account_holder, balance=0):
        super().__init__(account_number, account_holder, balance)
        self.__interest_rate = 0.7
    def withdraw(self):
        print("Sorry you cannot withdraw with a children's account")
    def deposit(self, amount):
        return super().deposit(amount)