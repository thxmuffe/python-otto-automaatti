"""This is a Python program simulating a cash-withdrawal automate
Please write your code in english (if possible)

THERE ARE MISSING PARTS ARE NAMED:
TASK1,
TASK2,
TASK3,... etc.
FILL IN THE MISSING PARTS UNTIL EVERYTHING WORKS"""

#### DO NOT CHANGE... _________________ ####
# This imports code and classes from account_manager.py
from account_manager import AccountManager

# This initializes the AccountManager
accounts = AccountManager()
#### ___________________________ ...END ####

# Program starts and asks for user's PIN-code
try_count = 0

# TASK1:
# add here logic:
#    program should ask for pin 3 times, and quit if pin code was not correct.
#    cosider using a while- or for-loop ... or goto??

# TASK2:
# add a suitable prompt for user. (suitable prompt: sopivanlainen kehoite teksti)
pincode = input("kerro...")

try_count += 1 # keep score, how many times user has tried to input PIN-code

if (accounts.findWithPinCode(pincode)):
    print("PIN oikein")

    # TASK3:
    # add here a call to "fetchBalance"-method in accounts-object, which returns the account balance
    # (balance: tilillä oleva summa)

    # TASK4:
    # add here code which prints the current balance for user

    # TASK5:
    # ask user what to do: WITHDRAWAL or EXIT

    # TASK6:
    # if user choce WITHDRAWAL, ask the amount and use the "Withdraw"-method
    # in accounts-object to update the account balance.
else:
    print("lukossa...") # 3: print a clear message for user that account is now locked.
