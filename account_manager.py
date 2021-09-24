class AccountManager:

    def __init__(self):
        self.pincode = 1234
        self.balance = 500 # this is in EUR.

    def findWithPinCode(self, code):
        return code == self.pincode

    def fetchBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount