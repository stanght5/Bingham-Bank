from account import Account

class Children_Account(Account):
    def __init__(self, account_number, account_holder, balance=0):
        super().__init__(account_number, account_holder, balance)
        self.__interest_rate = 0.7 / 100
    def get_interest_rate(self):
        return self.__interest_rate * 100
    def set_interest_rate(self, interest_rate):
        self.__interest_rate = interest_rate / 100
        return self.__interest_rate * 100
    def withdraw(self, amount):
        print("Sorry, you cannot withdraw from a children's account")
    def deposit(self, amount):
        return super().deposit(amount)
    def add_interest(self):
        interest_rate = self.get_interest_rate()
        interest = self.balance * interest_rate
        self.deposit(interest)
        return interest
    
my_childs_account = Children_Account(9124587748, "Bemdoo Maor")
my_childs_account.withdraw(3000)
my_childs_account.deposit(5000)
my_childs_account.add_interest()
my_childs_account.get_balance()
my_childs_account.display()