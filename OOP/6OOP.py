class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
    
    def get_balance(self):
        return self.balance

acc1 = Account(10000, 12321)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(20000)