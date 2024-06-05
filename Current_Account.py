from account import Account

class CurrentAccount(Account):
    def __init__(self, account_number, account_holder, balance=0):
        super().__init__(account_number, account_holder, balance)

current = CurrentAccount(221832374, "Adebayo Miracle", 2000)
current.deposit(500)
current.withdraw(1000)
current.display()
