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

if __name__ == "__main__":
    account = BankAccount("123456789", 1000)
    account.deposit(500)
    account.withdraw(200)
    account.check_balance()
    account.withdraw(1500)  
    account.deposit(-100)   
    account.withdraw(-50)   
    