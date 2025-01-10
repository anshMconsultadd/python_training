class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit invalid")
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal invalid")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}.")

    def check_balance(self):
        print(f"Current balance is {self.balance}.")
        return self.balance
    
    
class savingsAccount(BankAccount):
    def __init__(self, account_number, initial_balance=0, interest_rate=0):
        super().__init__(account_number, initial_balance)
        self.interest_rate = interest_rate

    def intrets_calculation(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest of {interest} added. New balance is {self.balance}.")

    def transaction_limits(self, amount):
        if amount > 10000:
            print("Transaction limit exceeded.")
            return
        else:
            self.balance -= amount
            print(f"Transaction of {amount} successful. New balance is {self.balance}.")
            return
        
class checkingAccount(BankAccount):
    def loan_eligibility(self, account_number, initial_balance=0):
        if self.balance < 1000:
            print("Loan not eligible.")
            return
        else:
            print("Loan eligible.")
            return
        


if __name__ == "__main__":
    account=BankAccount("123456789", 1000)  
    account.deposit(500)
    account.deposit(2000)

    sav_acc=savingsAccount("123456789", 1000, 0.1)
    sav_acc.deposit(500000)
    sav_acc.check_balance()
    