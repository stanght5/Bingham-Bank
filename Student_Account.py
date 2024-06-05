from account import Account


class StudentAccount(Account):
    def __init__(self, account_number, account_holder, balance=0):
        super().__init__(account_number, account_holder, balance)

    def deposit(self, amount):
        if amount > 50000:
            print("Deposit limit exceeded")
        else:
            super().deposit(amount)

    def withdraw(self, amount):
        if amount > 2000:
            print("Withdrawal limit exceeded")
        else:
            super().withdraw(amount)


student = StudentAccount(47382473876, "Asher", 3000)
student.deposit(1500)
student.withdraw(1000)
student.withdraw(100000)
student.deposit(200000)
student.display()
