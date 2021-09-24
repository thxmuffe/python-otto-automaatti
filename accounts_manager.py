class AccountsManager:

    def __init__(self):
        self.pincode = 1234

    def findWithPinCode(self, code):
        return code == self.pincode