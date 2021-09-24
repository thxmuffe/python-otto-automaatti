"""This is a Python program simulating a cash-withdrawal automate
Please write your code in english (if possible)

THERE ARE MISSING PARTS NUMBERED 1-10
FILL IN THE MISSING PARTS UNTIL EVERYTHING WORKS"""

#### DO NOT CHANGE... _________________ ####
from accounts_manager import AccountsManager # This imports code and classes from account_manager.py
accounts = AccountsManager()
#### ___________________________ ...END ####

# Program starts and asks for user's PIN-code
try_count = 0

# 1: add a suitable prompt for user. (suitable prompt: sopivanlainen kehoite teksti)
pincode = input("kerro...")

try_count += 1 # keep score, how many times user has tried to input PIN-code

# 2: add here logic:
#    program should ask for pin 3 times, and quit if pin code was not correct.
#    cosider using a while- or for-loop ... or goto??

if (accounts.findWithPinCode(pincode)):
    print("PIN oikein")
else:
    print("lukossa...") # 3: print a clear message for user that account is now locked.
