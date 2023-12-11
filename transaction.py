# transaction.py

from datetime import datetime

class Transaction:
    def __init__(self, source_account, destination_account, amount):
        self.timestamp = datetime.now()
        self.source_account = source_account
        self.destination_account = destination_account
        self.amount = amount

    def execute(self):
        if self.source_account.get_balance() >= self.amount:
            self.source_account.withdraw(self.amount)
            self.destination_account.deposit(self.amount)
            print("Transaction successful")
        else:
            print("Transaction failed: Insufficient funds")
