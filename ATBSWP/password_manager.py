import pyperclip
import sys

PASSWORD = {'email': 'this is my email password',
            'bofa': 'This is my bank password',
            'facebook': 'This is my facebook password'}

if len(sys.argv) < 2:
    print('Usage: python password_manager.py[account_name] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print("your password for " + account + " is copied, and ready to be pasted")
else:
    print("Your account do not match the record")
