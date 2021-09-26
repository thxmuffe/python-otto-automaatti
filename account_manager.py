import json

accounts_file = 'accounts.json' # path to settings

class AccountManager:

    def __init__(self):
        with open(accounts_file) as json_file:
            self.data = json.load(json_file)

    def findWithPinCode(self, code):
        for p in data['accounts']:
            if p['pincode'] == code:
                return True
        
        print("WARNING: Cannot find account with pin...")
        return False

    def fetchBalance(self):
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount

    def saveChanges():
        data = {}
        data['accounts'] = []
        data['accounts'].append({
            'id': self.accountId,
            'balance': self.balance,
            'pincode': self.pincode
        })

        with open(accounts_file, 'w') as outfile:
            json.dump(data, outfile)