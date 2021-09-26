import json

accounts_file = 'AccountData/accounts.json' # path to settings

class AccountManager:

    def __init__(self):
        with open(accounts_file) as json_file:
            self.data = json.load(json_file)

    def findWithPinCode(self, code):
        for account in self.data['accounts']:
            if account['pincode'] == code:
                self.current_account = account
                return True
        
        print("WARNING: Cannot find account with pin...")
        return False

    def fetchBalance(self):
        if (self.current_account):
            return self.current_account['balance']

    def saveChanges(self):
        with open(accounts_file, 'w') as outfile:
            json.dump(self.data, outfile)
            print("NOTIFICATION: Saved changes succesfully")

    def withdraw(self, amount):
        if (self.current_account):
            self.current_account['balance'] -= amount
            self.saveChanges()

