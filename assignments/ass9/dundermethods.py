# uild a class  Transaction  with dunder methods for comparing,
# adding, and representing transactions

class Transaction:
    def __init__(self, transaction_id, amount):
        self.transaction_id = transaction_id
        self.amount = amount

    def __eq__(self, other):
        return self.amount == other.amount 

    def __add__(self, other):
        return self.amount + other.amount

    def __str__(self):
        return f"Transaction ID: {self.transaction_id}, Amount: {self.amount}"
    
    def __repr__(self):
        return f"Transaction ID: {self.transaction_id}, Amount: {self.amount}"
    

    
Transaction1=Transaction(1, 1000)
# print(Transaction1)

Transaction2=Transaction(2, 1000)
# print(Transaction1==Transaction2)


print(dir(Transaction1))