# main.py

from account import Account
from transaction import Transaction

# Create accounts
account1 = Account(1, 1000)
account2 = Account(2, 500)

# Display initial balances
print("Initial Balances:")
print(f"Account {account1.account_number}: ${account1.get_balance()}")
print(f"Account {account2.account_number}: ${account2.get_balance()}")

# Perform a transaction
transaction = Transaction(account1, account2, 300)
transaction.execute()

# Display updated balances
print("\nUpdated Balances:")
print(f"Account {account1.account_number}: ${account1.get_balance()}")
print(f"Account {account2.account_number}: ${account2.get_balance()}")
