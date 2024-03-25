# # Abstraction
#
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.cloutch = False
#
#     def strts(self ):
#         self.acc = True
#         self.acc = True
#         print("car started")
#
# car1 = Car()
# car1.strts()
#
#
# #encapsulation

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc

    def debit(self, amount):
        self.balance -= amount
        print("RS.", amount, "was debited")
        print("Total balance =", self.get_balance())

    def credited(self, amount):
        self.balance += amount
        print("RS.", amount, "was credited")
        print("Total balance =", self.get_balance())

    def get_balance(self):
        return self.balance

ac11 = Account(265000, 1001)
ac11.debit(1000)
ac11.credited(5000)
ac11.debit(23000)
